
import ast
import json
import argparse
from pathlib import Path

MAX_CHUNK_LINES = 100
OVERLAP = 10

IGNORED_DIRS = {
    ".git", ".venv", "venv", "__pycache__", "node_modules"
}


def split_large_block(lines, start, end, file_path, symbol, block_type):
    chunks = []
    step = MAX_CHUNK_LINES - OVERLAP

    for chunk_start in range(start, end + 1, step):
        chunk_end = min(chunk_start + MAX_CHUNK_LINES - 1, end)

        chunks.append({
            "file": str(file_path),
            "symbol": symbol,
            "type": block_type,
            "start_line": chunk_start,
            "end_line": chunk_end,
            "content": "".join(lines[chunk_start - 1:chunk_end])
        })

        if chunk_end == end:
            break

    return chunks


def get_symbol(node):
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        return node.name

    if isinstance(node, (ast.Import, ast.ImportFrom)):
        return "imports"

    if isinstance(node, (ast.Assign, ast.AnnAssign)):
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        names = []

        for target in targets:
            if isinstance(target, ast.Name):
                names.append(target.id)

        return ", ".join(names) if names else "module_variable"

    if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant):
        return "module_docstring"

    return "module_context"


def get_node_type(node):
    if isinstance(node, ast.ClassDef):
        return "class"

    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        return "function"

    if isinstance(node, (ast.Import, ast.ImportFrom)):
        return "imports"

    return "module_context"


def chunk_file(file_path, repo_path):
    try:
        source = file_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        print(f"Skipping {file_path}: {error}")
        return []

    lines = source.splitlines(keepends=True)

    if not lines:
        return []

    try:
        tree = ast.parse(source)
    except SyntaxError:
        return split_large_block(
            lines,
            1,
            len(lines),
            file_path.relative_to(repo_path),
            "module_context",
            "module_context"
        )

    chunks = []
    relative_path = file_path.relative_to(repo_path)

    for node in tree.body:
        start = node.lineno

        # Include decorators in function/class chunks.
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if node.decorator_list:
                start = min(start, *(d.lineno for d in node.decorator_list))

        end = node.end_lineno
        symbol = get_symbol(node)
        block_type = get_node_type(node)

        if end - start + 1 <= MAX_CHUNK_LINES:
            chunks.append({
                "file": str(relative_path),
                "symbol": symbol,
                "type": block_type,
                "start_line": start,
                "end_line": end,
                "content": "".join(lines[start - 1:end])
            })
        else:
            chunks.extend(split_large_block(
                lines,
                start,
                end,
                relative_path,
                symbol,
                block_type
            ))

    return chunks


def chunk_repository(repo_path):
    chunks = []

    for file_path in sorted(repo_path.rglob("*.py")):
        if any(part in IGNORED_DIRS for part in file_path.relative_to(repo_path).parts):
            continue

        chunks.extend(chunk_file(file_path, repo_path))

    return chunks


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("repository", type=Path)
    parser.add_argument("-o", "--output", type=Path, default=Path("chunks.json"))
    args = parser.parse_args()

    repo_path = args.repository.resolve()

    if not repo_path.is_dir():
        parser.error(f"Repository directory does not exist: {repo_path}")

    chunks = chunk_repository(repo_path)

    with args.output.open("w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)

    print(f"Generated {len(chunks)} chunks")
    print(f"Output: {args.output}")


if __name__ == "__main__":
    main()
