# 修复版。
import requests

# 离线构造响应，观察状态检查的行为。
reply = requests.Response()
reply.status_code = 200
reply.raise_for_status()
print(reply.status_code)
