from http.server import (
    BaseHTTPRequestHandler,
    ThreadingHTTPServer,
)
from threading import Thread

import requests


class DemoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 用固定的本地样本练习 JSON 响应。
        body = b'{"name": "notes.md"}'
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        # 输出留给客户端的状态码和字段值。
        pass


with ThreadingHTTPServer(("127.0.0.1", 0), DemoHandler) as server:
    worker = Thread(target=server.serve_forever)
    worker.start()
    try:
        host, port = server.server_address[:2]
        with requests.Session() as session:
            session.trust_env = False
            response = session.get(
                f"http://{host}:{port}/", timeout=2
            )
            response.raise_for_status()
            print(response.status_code, response.json()["name"])
    finally:
        server.shutdown()
        worker.join()
