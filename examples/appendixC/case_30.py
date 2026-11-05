# 修复版。
# 空集合显式调用 set 创建。
seen = set()
seen.add("notes.md")
print(type(seen).__name__, "notes.md" in seen)
