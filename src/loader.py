from pathlib import Path


def load_file(file_name: str) -> str:
    """读取指定文件的内容，返回文本字符串"""
    file_path = Path(__file__).parent.parent / file_name
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
