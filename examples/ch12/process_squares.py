from concurrent.futures import ProcessPoolExecutor
from multiprocessing import get_context


def square(value):
    # 顶层函数便于子进程导入。
    return value * value


if __name__ == "__main__":
    with ProcessPoolExecutor(
        max_workers=2, mp_context=get_context("spawn")
    ) as pool:
        print(list(pool.map(square, [2, 3, 4])))
