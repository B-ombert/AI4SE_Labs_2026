# Repository Chunking Report

The goal of this task was to implement a simple Python tool that splits a repository into chunks for future use in a RAG system.

The tool uses Python's **AST module** to identify top-level classes, functions, imports, and module-level statements. Each element is stored as a separate chunk to preserve the logical structure of the source code.

The maximum chunk size is **100 lines**. Larger blocks are split by line count with a **10-line overlap** to preserve context between consecutive chunks. If a Python file cannot be parsed, the tool falls back to line-based splitting.

Each chunk is stored as a JSON object containing:
- File path
- Symbol name
- Chunk type
- Start and end line
- Source code content

The script recursively processes Python files, including tests, while excluding directories such as `.git`, `.venv`, and `__pycache__`.

The output is stored in `chunks.json`. The current execution generated **297 chunks**.

This approach provides a simple, structured representation of the repository while preserving enough source-code context for future RAG retrieval.