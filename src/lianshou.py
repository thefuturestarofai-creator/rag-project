import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("SILICONFLOW_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.siliconflow.cn/v1"
)

response = client.chat.completions.create(
    model="Qwen/Qwen2.5-7B-Instruct",       # ← 聊天模型名
    messages=[
        {"role": "user", "content": "你是什么模型？"}
    ]
)

print(response.choices[0].message.content)
