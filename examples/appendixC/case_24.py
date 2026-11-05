# 修复版。
import socket

# 端口 0 交给操作系统分配可用的临时端口。
with socket.socket() as listener:
    listener.bind(("127.0.0.1", 0))
    print(listener.getsockname()[1] > 0)
