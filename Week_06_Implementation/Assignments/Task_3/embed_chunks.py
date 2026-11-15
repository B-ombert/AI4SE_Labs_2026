
import json
from pathlib import Path

from sentence_transformers import SentenceTransformer


# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "Task_2" / "chunks.json"
OUTPUT_FILE = Path(__file__).resolve().parent / "embeddings.json"

# Embedding model
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


def create_embedding_text(chunk):
    """Combine chunk metadata and source code into one text."""
    return (
        f"Type: {chunk.get('type', '')}\n"
        f"Symbol: {chunk.get('symbol', '')}\n"
        f"File: {chunk.get('file', '')}\n\n"
        f"Content:\n{chunk.get('content', '')}"
    )


def main():
    # Load input chunks
    if not INPUT_FILE.is_file():
        print(f"Error: Input file not found: {INPUT_FILE}")
        return

    try:
        with INPUT_FILE.open("r", encoding="utf-8") as file:
            chunks = json.load(file)
    except json.JSONDecodeError as error:
        print(f"Error: Invalid JSON: {error}")
        return

    if not isinstance(chunks, list):
        print("Error: Expected a JSON list of chunks.")
        return

    if not chunks:
        print("No chunks found.")
        return

    # Prepare texts for embedding
    texts = [create_embedding_text(chunk) for chunk in chunks]

    # Load model once
    print(f"Loading model: {MODEL_NAME}")
    model = SentenceTransformer(MODEL_NAME)

    # Generate embeddings in batches
    print(f"Generating embeddings for {len(chunks)} chunks...")

    embeddings = model.encode(
        texts,
        batch_size=32,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    # Combine original chunks with their embeddings
    results = []

    for chunk, embedding in zip(chunks, embeddings):
        result = chunk.copy()
        result["embedding"] = embedding.tolist()
        results.append(result)

    # Save results
    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(results, file, indent=2, ensure_ascii=False)

    print(f"\nGenerated {len(results)} embeddings.")
    print(f"Embedding dimensions: {len(embeddings[0])}")
    print(f"Output: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
