def read_retries(raw):
    # 转换失败和超出范围，都是输入无效。
    value = int(raw)
    if value < 0:
        raise ValueError("重试次数不能小于零")
    return value


try:
    count = read_retries("-1")
except ValueError as error:
    print(error)
else:
    print("重试次数", count)
finally:
    # 即使转入 except，这一行也会执行。
    print("输入检查结束")
