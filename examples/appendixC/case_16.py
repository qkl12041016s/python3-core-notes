# 修复版。
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    path = Path(folder)
    # 先按目标类型选择处理方式。
    print("这是目录" if path.is_dir() else "这是文件")
