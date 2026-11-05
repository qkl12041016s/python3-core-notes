def fibonacci(count):
    # 只保留相邻两项，用它们计算下一项。
    left, right = 0, 1
    for _ in range(count):
        yield left
        left, right = right, left + right


print(list(fibonacci(7)))
