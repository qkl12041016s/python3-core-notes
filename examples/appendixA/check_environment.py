import sys
from pathlib import Path

# 三个现场信息，核对解释器与相对路径的起点。
print(sys.version.split()[0])
print(sys.executable)
print(Path.cwd())
