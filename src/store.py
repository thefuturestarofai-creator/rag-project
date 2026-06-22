import chromadb

chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="my_docs")


def add_document(doc_id: str, content: str, embedding: list[float]):
    """把文档的原始文本和向量存入 ChromaDB"""
    collection.add(
        ids=[doc_id],
        documents=[content],
        embeddings=[embedding]
    )


def search(query_embedding: list[float], n_results: int = 3) -> list[str]:
    """用问题向量去 ChromaDB 检索最相似的文档，返回文档列表"""
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )
    return results["documents"][0]
