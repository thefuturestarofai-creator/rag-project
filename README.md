# RAG 知识库问答系统

基于检索增强生成（RAG）的智能问答系统，支持本地文档导入、语义向量检索、大模型生成回答。

## 技术栈

| 组件 | 技术 |
|---|---|
| 向量化模型 | BAAI/bge-m3（硅基流动平台） |
| 生成模型 | Qwen2.5-7B-Instruct（硅基流动平台） |
| 向量数据库 | ChromaDB |
| OpenAI SDK | openai（兼容硅基流动 API） |
| 包管理 | uv |

## 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/thefuturestarofai-creator/rag-project.git
cd rag-project

# 2. 安装依赖（需要先安装 uv）
uv sync

# 3. 配置 API Key
cp .env.example .env
# 编辑 .env，填入你的硅基流动 API Key

# 4. 运行
uv run python src/main.py
```

## 项目结构

```
rag-project/
├── src/
│   ├── main.py        # RAG 主流程入口
│   ├── config.py      # 配置管理（API Key 等）
│   ├── loader.py      # 文档加载模块
│   ├── embedder.py    # 文本向量化模块
│   ├── store.py       # 向量数据库操作模块
│   └── generator.py   # 大模型生成模块
├── test.txt           # 示例知识文档
├── .env.example       # API Key 配置示例
├── pyproject.toml     # 项目依赖配置
└── .gitignore
```

## 工作流程

```
读取文档 → 文本向量化(Embedding) → 存入向量数据库(ChromaDB)
                                          ↓
用户提问 → 问题向量化 → 向量相似度检索 → 取出相关文档片段
                                          ↓
                        拼接 Prompt（参考资料 + 问题）→ 大模型生成回答
```

## TODO

- [ ] FastAPI 接口封装
- [ ] LangChain 编排集成
- [ ] 混合检索 + 重排序
- [ ] 流式输出
- [ ] Docker 部署
- [ ] Streamlit / Gradio 前端界面
