# 修复版。
# 每条字符串各自清理，结果仍是一张列表。
files = [" notes.md ", " todo.md "]
print([name.strip() for name in files])
