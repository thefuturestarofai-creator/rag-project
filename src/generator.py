from src.config import client


def generate_answer(question: str, context_docs: list[str]) -> str:
    """把检索到的文档和问题拼成 Prompt，调用大模型生成回答"""
    context = "\n\n".join(context_docs)

    prompt = f"""请根据以下参考资料来回答问题。如果资料中没有相关信息，请说明你不确定。

【参考资料】
{context}

【问题】
{question}
"""

    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-7B-Instruct",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
