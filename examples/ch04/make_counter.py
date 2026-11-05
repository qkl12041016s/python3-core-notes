def make_counter(start: int):
    count = start

    def advance() -> int:
        # 重新绑定外层 count，要明确写 nonlocal。
        nonlocal count
        count += 1
        return count

    return advance


counter = make_counter(10)
print(counter())
print(counter())
