#CHUNKING

import os 
from sentence_transformers import SentenceTransformer
import chromadb

SOURCE_DIR = "/workspaces/Arabic-Health-Checker/data/sources"

def load_documents() -> list [dict] : #reads all the .txt files 
    """
    Reads every .txt file in data/sources and returns a list 
    of {"source" : filename, "text" : full file content}
    """

    documents = []
    for filename in os.listdir(SOURCE_DIR) :
        if filename.endswith(".txt") :
            filepath = os.path.join(SOURCE_DIR, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
            documents.append({"source":filename, "text" : text})
    return documents


def chunk_text(text: str, max_chars: int = 300) -> list[str] : #splits each document's text into pieces of roughly 300 chars 
    """
    Splits text into chunks of roughly max_chars, breaking at sentence
    boundaries (".")
    """ 

    sentences = text.split("|") if "|" in text else text.split(".")
    chunks = []
    current = ""

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
        if len(current) + len(sentence) < max_chars:
            current += sentence + ". "
        else :
            if current:
                chunks.append(current.strip())
            current = sentence + ". "
    
    if current : 
        chunks.append(current.strip())
    
    return chunks 

def build_index () : 
    print ("Loading embedding model..")
    model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

    client = chromadb.PersistentClient(path="data/chroma_db")
    collection = client.get_or_create_collection("health_sources")

    docs = load_documents()
    chunk_id = 0

    for doc in docs :
        chunks = chunk_text(doc["text"])
        for chunk in chunks : 
            embedding = model.encode(chunk).tolist()
            collection.add(
                ids=[str(chunk_id)],
                embeddings = [embedding],
                documents = [chunk],
                metadatas = [{"source" : doc["source"]}]
            )

            chunk_id += 1

    print(f"Indexed {chunk_id} chunks into ChromaDB")

if __name__ == "__main__" : 
    build_index()