# 修复版。
# 拼成新字符串，原值留作对照。
s = "hello"
original = s
s = "H" + s[1:]
print(s, original)
