import sys
from pathlib import Path

# 把项目根目录加入 Python 搜索路径，确保 import 能找到 src 包
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.loader import load_file
from src.embedder import get_embedding
from src.store import add_document, search
from src.generator import generate_answer


def main():
    # 1. 读取文档
    content = load_file("test.txt")

    # 2. 向量化并存入数据库
    vector = get_embedding(content)
    add_document(doc_id="doc1", content=content, embedding=vector)

    # 3. 用户提问 → 向量化 → 检索
    question = "FastAPI是什么框架？"
    query_vector = get_embedding(question)
    results = search(query_vector)

    # 4. 大模型生成回答
    answer = generate_answer(question, results)
    print("AI 回答：", answer)


if __name__ == "__main__":
    main()
