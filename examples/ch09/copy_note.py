from pathlib import Path
from shutil import copy2
from tempfile import TemporaryDirectory

# 在临时目录造一份 UTF-8 样本。
with TemporaryDirectory() as folder:
    root = Path(folder)
    source = root / "notes.txt"
    source.write_text("同步完成", encoding="utf-8")

    # 先建目标目录，再把文件复制过去。
    destination = root / "backup" / source.name
    destination.parent.mkdir()
    copy2(source, destination)
    print(destination.relative_to(root).as_posix())
    print(destination.read_text(encoding="utf-8"))
