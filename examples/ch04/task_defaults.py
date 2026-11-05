# 复现两次调用共用同一个默认列表。
def add_shared(name, tasks=[]):
    tasks.append(name)
    return tasks


# 省略清单时，每次调用都创建一份。
def add_task(name, tasks=None):
    if tasks is None:
        tasks = []
    tasks.append(name)
    return tasks


first = add_shared("notes.md")
second = add_shared("todo.md")
print(first, second)
print(add_task("notes.md"), add_task("todo.md"))
