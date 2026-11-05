from functools import wraps
from time import perf_counter


def timer(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        started = perf_counter()
        try:
            return function(*args, **kwargs)
        finally:
            print("耗时已记录", perf_counter() >= started)
    return wrapped


@timer
def add(left, right):
    # 原函数继续负责计算。
    return left + right


print(add(2, 3))
print(add.__name__)
