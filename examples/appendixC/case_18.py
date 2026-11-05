# 修复版。
# 两端约定 UTF-8，检查一次往返。
text = "雪"
print(text.encode("utf-8").decode("utf-8"))
