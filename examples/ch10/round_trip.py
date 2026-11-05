import csv
import io
import json

row = {"name": "notes.md", "retries": 3}

# JSON 的数字字段读回后仍是整数。
json_row = json.loads(json.dumps(row))

# CSV 默认读回字符串，先在内存里跑通读写。
stream = io.StringIO(newline="")
writer = csv.DictWriter(stream, fieldnames=["name", "retries"])
writer.writeheader()
writer.writerow(row)
stream.seek(0)
csv_row = next(csv.DictReader(stream))

print(type(json_row["retries"]).__name__)
print(type(csv_row["retries"]).__name__)
