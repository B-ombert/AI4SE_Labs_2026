
import json
from pathlib import Path

from sentence_transformers import SentenceTransformer


BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "embeddings.json"

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

model = None


def load_model():
    global model

    if model is None:
        model = SentenceTransformer(MODEL_NAME)

    return model


def search_chunks(query, n=5):
    if not INPUT_FILE.is_file():
        raise FileNotFoundError(INPUT_FILE)

    with INPUT_FILE.open("r", encoding="utf-8") as file:
        chunks = json.load(file)

    if not chunks:
        return []

    model = load_model()

    query_embedding = model.encode(
        query,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    results = []

    for chunk in chunks:
        embedding = chunk["embedding"]

        if len(embedding) != len(query_embedding):
            raise ValueError(
                f"Embedding dimension mismatch in {chunk['file']}"
            )

        similarity = sum(
            a * b for a, b in zip(query_embedding, embedding)
        )

        result = chunk.copy()
        result["similarity"] = float(similarity)

        results.append(result)

    results.sort(
        key=lambda chunk: chunk["similarity"],
        reverse=True
    )

    return results[:n]


def main():
    query = input("Enter your task: ").strip()

    if not query:
        print("Empty task.")
        return

    try:
        n = int(input("Enter the number of chunks to retrieve: "))
    except ValueError:
        print("Invalid number.")
        return

    if n <= 0:
        print("Number of results must be positive.")
        return

    results = search_chunks(query, n)

    for rank, chunk in enumerate(results, start=1):
        print("=" * 70)
        print(f"Rank: {rank}")
        print(f"Similarity: {chunk['similarity']:.4f}")
        print(f"File: {chunk['file']}")
        print(f"Symbol: {chunk['symbol']}")
        print(f"Type: {chunk['type']}")
        print(f"Lines: {chunk['start_line']}-{chunk['end_line']}")
        print("\nContent:")
        print(chunk["content"])


if __name__ == "__main__":
    main()
