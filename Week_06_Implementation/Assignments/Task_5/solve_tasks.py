import argparse
import ast
import json
import os
import sys
from pathlib import Path
import textwrap

from dotenv import load_dotenv
from openai import OpenAI


# Load environment variables from Task_5/.env
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


# Project paths
ASSIGNMENTS_DIR = BASE_DIR.parent
REPO_DIR = ASSIGNMENTS_DIR / "AI4SE_Playground"
TASKS_FILE = ASSIGNMENTS_DIR / "missing_code.json"

TASK_3_DIR = ASSIGNMENTS_DIR / "Task_3"
sys.path.insert(0, str(TASK_3_DIR))

from search_chunks import search_chunks


# LLM configuration
MODEL_NAME = "gpt-6-luna"
BASE_URL = os.getenv(
    "OPENAI_BASE_URL",
    "https://api.openai.com/v1"
)


def create_client():
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Check your .env file."
        )

    return OpenAI(
        api_key=api_key,
        base_url=BASE_URL
    )


def find_class(tree, class_name):
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == class_name:
            return node

    raise ValueError(f"Class '{class_name}' not found.")


def find_method(class_node, method_name):
    for node in class_node.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.name == method_name:
                return node

    raise ValueError(
        f"Method '{method_name}' not found "
        f"in class '{class_node.name}'."
    )


def get_class_source(source, class_node):
    return ast.get_source_segment(source, class_node)


def generate_method(client, task, chunks, class_source):
    context = "\n\n".join(
        f"--- Chunk {i} ---\n"
        f"File: {chunk['file']}\n"
        f"Symbol: {chunk['symbol']}\n"
        f"Content:\n{chunk['content']}"
        for i, chunk in enumerate(chunks, start=1)
    )

    prompt = f"""
Implement the missing Python method described below.

Target:
File: {task['file']}
Class: {task['class']}
Method: {task['method']}

Method documentation:
{task['docstring']}

Current class source:
{class_source}

Relevant repository context retrieved using semantic search:
{context}

Requirements:
- Return only the complete Python method definition.
- Do not use Markdown code fences.
- Keep the original method name and signature.
- Preserve the supplied docstring.
- Do not implement unrelated methods.
- Follow the existing repository conventions.
- Handle relevant edge cases.
- Do not invent attributes or methods unless supported by context.
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an experienced Python developer. "
                    "Implement methods accurately using the supplied "
                    "repository context."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response.choices[0].message.content

    if not content:
        raise RuntimeError("The model returned an empty response.")

    return content.strip()


def clean_generated_code(code):
    code = code.strip()

    if code.startswith("```"):
        lines = code.splitlines()
        lines = lines[1:]

        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]

        code = "\n".join(lines)

    return textwrap.dedent(code).strip()


def validate_method(code, original_method):
    code = clean_generated_code(code)

    try:
        tree = ast.parse(code)
    except SyntaxError as error:
        raise ValueError(
            f"Generated code contains invalid Python: {error}"
        )

    methods = [
        node for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    ]

    if len(methods) != 1:
        raise ValueError(
            "The model must return exactly one method definition."
        )

    generated = methods[0]

    if generated.name != original_method.name:
        raise ValueError(
            f"Expected method '{original_method.name}', "
            f"got '{generated.name}'."
        )

    if type(generated) is not type(original_method):
        raise ValueError(
            "The generated method has a different async type."
        )

    original_args = [
        arg.arg
        for arg in (
            original_method.args.posonlyargs
            + original_method.args.args
        )
    ]

    generated_args = [
        arg.arg
        for arg in (
            generated.args.posonlyargs
            + generated.args.args
        )
    ]

    if original_args != generated_args:
        raise ValueError(
            f"Method signature mismatch: "
            f"{original_args} != {generated_args}"
        )

    return code


def prepare_replacement(code, original_method, source_lines):
    code = clean_generated_code(code)

    original_line = source_lines[original_method.lineno - 1]
    indentation = len(original_line) - len(original_line.lstrip())

    indent = " " * indentation

    return "\n".join(
        indent + line if line.strip() else ""
        for line in code.splitlines()
    )


def apply_changes(generated_methods):
    grouped = {}

    for item in generated_methods:
        grouped.setdefault(item["file"], []).append(item)

    backup_dir = BASE_DIR / "backups"

    for relative_path, methods in grouped.items():
        source_path = REPO_DIR / relative_path

        if not source_path.is_file():
            raise FileNotFoundError(source_path)

        original_source = source_path.read_text(encoding="utf-8")
        source_lines = original_source.splitlines()

        tree = ast.parse(original_source)

        replacements = []

        for item in methods:
            class_node = find_class(tree, item["class"])
            method_node = find_method(class_node, item["method"])

            replacement = prepare_replacement(
                item["code"],
                method_node,
                source_lines
            )

            replacements.append((
                method_node.lineno - 1,
                method_node.end_lineno,
                replacement
            ))

        # Replace methods from bottom to top.
        for start, end, replacement in sorted(
            replacements,
            key=lambda item: item[0],
            reverse=True
        ):
            source_lines[start:end] = replacement.splitlines()

        updated_source = "\n".join(source_lines) + "\n"

        # Validate the complete updated file.
        ast.parse(updated_source)

        # Create backup before modifying the original file.
        backup_path = backup_dir / relative_path
        backup_path.parent.mkdir(parents=True, exist_ok=True)

        backup_path.write_text(
            original_source,
            encoding="utf-8"
        )

        source_path.write_text(
            updated_source,
            encoding="utf-8"
        )

        print(f"Updated: {relative_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Implement missing methods using RAG and an LLM."
    )

    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write generated methods into repository source files."
    )

    args = parser.parse_args()

    if not TASKS_FILE.is_file():
        raise FileNotFoundError(
            f"Missing tasks file: {TASKS_FILE}"
        )

    with TASKS_FILE.open("r", encoding="utf-8") as file:
        tasks = json.load(file)

    client = create_client()

    generated_methods = []

    print(f"Processing {len(tasks)} tasks using {MODEL_NAME}.")

    for index, task in enumerate(tasks, start=1):
        print(
            f"\n[{index}/{len(tasks)}] "
            f"{task['class']}.{task['method']}"
        )

        source_path = REPO_DIR / task["file"]

        if not source_path.is_file():
            print(f"ERROR: Source file not found: {source_path}")
            continue

        try:
            source = source_path.read_text(encoding="utf-8")
            tree = ast.parse(source)

            class_node = find_class(tree, task["class"])
            method_node = find_method(class_node, task["method"])

            class_source = get_class_source(source, class_node)

            query = (
                f"Implement {task['class']}.{task['method']} "
                f"in {task['file']}. "
                f"{task['docstring']}"
            )

            chunks = search_chunks(query, n=5)

            if not chunks:
                print("WARNING: No relevant chunks found.")
                continue

            print(f"Retrieved {len(chunks)} relevant chunks.")

            code = generate_method(
                client,
                task,
                chunks,
                class_source
            )

            code = validate_method(code, method_node)

            generated_methods.append({
                "file": task["file"],
                "class": task["class"],
                "method": task["method"],
                "code": code
            })

            print("Method generated and validated.")

        except Exception as error:
            print(f"ERROR: {error}")

    output_file = BASE_DIR / "generated_methods.json"

    with output_file.open("w", encoding="utf-8") as file:
        json.dump(
            generated_methods,
            file,
            indent=4,
            ensure_ascii=False
        )

    print(
        f"\nGenerated {len(generated_methods)} "
        f"out of {len(tasks)} methods."
    )

    print(f"Generated methods saved to: {output_file}")

    if args.apply:
        if generated_methods:
            apply_changes(generated_methods)
            print("\nValidated changes were applied.")
        else:
            print("No methods to apply.")
    else:
        print(
            "\nDry run: source files were not modified. "
            "Use --apply to apply generated methods."
        )


if __name__ == "__main__":
    main()
