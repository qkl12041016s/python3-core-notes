total = 0
for value in [2, 3, 5]:
    # 断点停在这里时，total 还是本次相加前的值。
    total += value
    print(value, total)

# 输出应依次为 2 2、3 5、5 10。
print("最终", total)
