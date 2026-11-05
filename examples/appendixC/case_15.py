# 修复版。
from pathlib import Path
from tempfile import TemporaryDirectory

# 输入在明确的目录创建，再从同一路径读取。
with TemporaryDirectory() as folder:
    path = Path(folder) / "note.txt"
    path.write_text("ready", encoding="utf-8")
    print(path.read_text(encoding="utf-8"))
