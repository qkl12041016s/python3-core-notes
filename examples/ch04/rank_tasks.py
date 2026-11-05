# 同一批任务先筛选，再排序和提取名称。
tasks = [("notes.md", 2), ("todo.md", 1), ("draft.md", 2)]
selected = filter(lambda task: task[1] >= 2, tasks)
ordered = sorted(selected, key=lambda task: task[0])
names = list(map(lambda task: task[0], ordered))
print(names)
print(tasks[0])  # 原列表中的顺序没有被改动。
