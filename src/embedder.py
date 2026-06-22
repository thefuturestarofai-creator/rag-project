from src.config import client


def get_embedding(text: str) -> list[float]:
    """调用 Embedding 模型，把文本转成向量"""
    response = client.embeddings.create(
        model="BAAI/bge-m3",
        input=text
    )
    return response.data[0].embedding
