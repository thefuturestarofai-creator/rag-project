from pathlib import Path
from openai import OpenAI
import chromadb
import os
from dotenv import load_dotenv

load_dotenv()  # 读取 .env 文件，加载到系统环境变量
api_key = os.getenv("SILICONFLOW_API_KEY")  # 取出密钥值

## 1. 读取文件内容
file_path = Path(__file__).parent / "test.txt"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()
    
## 2. 调用ai模型，将文本向量化
client = OpenAI(
    api_key= api_key,
    base_url="https://api.siliconflow.cn/v1"
)

response = client.embeddings.create(          # ← 注意这里是 embeddings
    model="BAAI/bge-m3",                      # ← 向量化模型名
    input=content                             # ← 传入文本内容，不是文件名
)

vector = response.data[0].embedding           # 拿到向量（一串浮点数）


## 3. 将向量化的数据存入向量数据库中
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="my_docs")
collection.add(
    ids=["doc1"],              # 唯一标识，自己定，用来找/删/改
    documents=[content],       # 原始文本（存着方便后面看是什么内容）
    embeddings=[vector]        # 你算好的向量
)

## 4. 查询：把问题也向量化，再去搜索
question = "FastAPI是什么框架？"                           # ← 替换成你的问题
query_response = client.embeddings.create(
    model="BAAI/bge-m3",
    input=question
)
query_vector = query_response.data[0].embedding     # 问题的向量

results = collection.query(
    query_embeddings=[query_vector],   # 用问题向量去查
    n_results=3                        # 返回最相似的 3 条
)


## 5. 调用大模型，把检索结果和问题一起发给它，让AI精加工后回答
# 复用第2步已有的 client，不用重复创建

# 把检索到的文档拼成一段上下文
retrieved_docs = results["documents"][0]       # 取出检索到的文档列表
context = "\n\n".join(retrieved_docs)          # 用换行拼成一整段

# 组装 prompt：告诉AI"根据以下资料回答问题"
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

print("AI 回答：", response.choices[0].message.content)