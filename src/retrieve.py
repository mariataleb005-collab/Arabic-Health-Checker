from sentence_transformers import SentenceTransformer
import chromadb

import streamlit as st

@st.cache_resource
def get_model():
    return SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

@st.cache_resource
def get_collection():
    client = chromadb.PersistentClient(path="data/chroma_db")
    return client.get_or_create_collection("health_sources")

model = get_model()
collection = get_collection()

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

