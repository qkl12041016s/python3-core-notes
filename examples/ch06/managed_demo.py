from contextlib import contextmanager


@contextmanager
def checked_resource():
    print("取得资源")
    try:
        yield "notes.md"
    finally:
        # 离开 with 时统一收尾。
        print("归还资源")


with checked_resource() as name:
    print("处理", name)
