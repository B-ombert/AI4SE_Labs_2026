# Task 4 – Embedding Matching and Retrieval

## Overview

The goal of this task was to implement a mechanism for matching an input task with previously stored code chunks using their embeddings.

## Design Decisions

The implementation reuses the embeddings generated in the previous task and stored in `embeddings.json`. This avoids recalculating embeddings for all repository chunks every time a search is performed.

The input task is provided as text and converted into a 384-dimensional embedding using the same `sentence-transformers/all-MiniLM-L6-v2` model used during embedding generation.

To measure the relevance of stored chunks, the implementation uses **cosine similarity**. Since all embeddings are normalized, cosine similarity can be calculated efficiently using the dot product.

All stored chunks are compared with the input embedding and sorted in descending order of similarity.

The user can specify the number of results (`n`) to retrieve. The program returns the `n` chunks with the highest similarity scores, including their metadata and source code.

## Conclusion

The implemented matching mechanism enables semantic retrieval of relevant code chunks based on an input task. It reuses existing embeddings, supports a configurable number of results, and does not require an additional vector database.