# 修复版。
# 用默认值明确表示这次已经读到结尾。
iterator = iter(["notes.md"])
print(next(iterator, "结束"))
print(next(iterator, "结束"))
