from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    # 先写 UTF-8，再按同样编码读回。
    path = Path(folder) / "note.txt"
    with path.open("w", encoding="utf-8") as stream:
        stream.write("雪落长安无声")

    with path.open("r", encoding="utf-8") as stream:
        print(stream.read())
