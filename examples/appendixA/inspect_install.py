import importlib.util
import sys

# 先找解释器，再看当前环境能否定位包。
print("Python:", sys.executable)
print("Version:", sys.version.split()[0])
spec = importlib.util.find_spec("requests")
print("requests:", None if spec is None else spec.origin)
