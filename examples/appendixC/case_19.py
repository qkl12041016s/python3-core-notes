# 修复版。
import json

# 由序列化函数生成完整 JSON，再读回来。
encoded = json.dumps({"name": "notes.md"})
print(json.loads(encoded)["name"])
