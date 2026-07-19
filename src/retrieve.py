from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
client = chromadb.PersistentClient(path = "/workspaces/Arabic-Health-Checker/data/chroma_db")
collection = client.get_or_create_collection("health_sources")

def retrieve_relevant_chunks(claim: str, k:int=3) -> list[dict]:
    """
    Given a health claim, returns the top-k most relevant chunks
    from the source library, each with its text and source filename
    """

    query_embedding = model.encode(claim).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    chunks = []
    for text, metadata in zip(results["documents"][0], results["metadatas"][0]) :
        chunks.append({"text": text, "source":metadata["source"]})

    return chunks


if __name__ == "__main__":
    test_claim = "الزنجبيل يشفي من السرطان"
    results = retrieve_relevant_chunks(test_claim)

    print(f"Claim: {test_claim}\n")
    for i , r in enumerate(results):
        print(f"Match {i+1} (from {r['source']}):")
        print(r["text"])
        print()

