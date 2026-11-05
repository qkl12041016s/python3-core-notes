# 修复版。
import socket
import requests

# 本机监听但不返回 HTTP，用来演练读取超时。
with socket.socket() as listener, requests.Session() as session:
    session.trust_env = False
    listener.bind(("127.0.0.1", 0))
    listener.listen()
    port = listener.getsockname()[1]
    try:
        session.get(f"http://127.0.0.1:{port}/", timeout=0.05)
    except requests.Timeout:
        print("记录超时，交给上层处理")
