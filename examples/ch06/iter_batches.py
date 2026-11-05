# 每次只取出当前一批文件。
def iter_batches(files, size):
    for start in range(0, len(files), size):
        print("准备第", start // size + 1, "批")
        yield files[start : start + size]


# 依次拉取两批，观察日志和结果的顺序。
batches = iter_batches(["notes.md", "todo.md", "draft.md"], 2)
print("生成器已建立")
print(next(batches))
print(next(batches))
