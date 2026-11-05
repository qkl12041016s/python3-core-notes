# 修复版。
# 本例元素为字符串，复制外层足够保留名单。
original = ["notes.md"]
backup = original.copy()
original.append("todo.md")
print(len(original), len(backup))
