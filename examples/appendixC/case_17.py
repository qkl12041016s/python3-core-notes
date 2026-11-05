# 修复版。
# 样本的来源约定为 Latin-1。
raw = b"\xff"
text = raw.decode("latin-1")
print(text)
assert text.encode("latin-1") == raw
