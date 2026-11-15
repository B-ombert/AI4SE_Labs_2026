# Task 3 – Code Embeddings and Retrieval

## Overview

The goal of this task was to generate numerical embeddings for the code chunks created in Task 2, store them together with the original chunks, and implement semantic search based on these embeddings.

## Embedding Model

The implementation uses the **`sentence-transformers/all-MiniLM-L6-v2`** model from Sentence Transformers.

This model was selected because it is lightweight, relatively fast, and suitable for generating semantic embeddings from text. It produces a **384-dimensional vector** for each input.

The model is loaded once during each script execution and automatically downloads its files on the first run.

## Chunk Representation

Before generating an embedding, each chunk is converted into a text representation containing:

- Chunk type
- Symbol name
- File path
- Source code content

Including metadata provides additional context about the code and helps the model distinguish between different types of code elements.

## Embedding Generation and Storage

The `embed_chunks.py` script reads the chunks from `Task_2/chunks.json` and generates an embedding for each one.

The embeddings are generated in batches of 32. They are also normalized using `normalize_embeddings=True`, which allows cosine similarity to be calculated efficiently using the dot product.

Each generated embedding is stored together with its original chunk metadata and source code in a JSON file named `embeddings.json`.

The execution generated **297 embeddings**, each containing **384 numerical values**.

## Semantic Search

The `search_chunks.py` script implements semantic search over the stored chunks.

It accepts a text query, converts it into an embedding using the same model, and compares it with all stored chunk embeddings.

Cosine similarity is calculated using the dot product because all embeddings are normalized. The results are sorted in descending order of similarity, and the five most relevant chunks are displayed.

Each result includes its similarity score, file path, symbol name, chunk type, line range, and source code.

## Conclusion

The implementation successfully generates and stores embeddings for all 297 code chunks. It also provides a simple semantic search mechanism that retrieves relevant code chunks based on the meaning of a text query rather than exact keyword matching.

The generated embeddings are stored in JSON, avoiding the need for an additional vector database for this repository-sized dataset.