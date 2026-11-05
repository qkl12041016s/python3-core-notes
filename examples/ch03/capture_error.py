import io
import logging

# 演示专用日志对象，避免重复挂接处理器。
stream = io.StringIO()
logger = logging.getLogger("capture-demo")
logger.handlers.clear()
logger.propagate = False
logger.setLevel(logging.ERROR)
logger.addHandler(logging.StreamHandler(stream))

try:
    int("broken")
except ValueError:
    logger.exception("输入转换失败")

# 核对消息和异常栈都进入了日志。
print("输入转换失败" in stream.getvalue())
print("ValueError" in stream.getvalue())
