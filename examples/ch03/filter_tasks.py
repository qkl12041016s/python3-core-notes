# 逐条筛选，输出清单和原清单分别保留。
files = ["notes.md", "cache.tmp", "draft.tmp", "todo.md"]
kept = []
for name in files:
    if name.endswith(".tmp"):
        continue
    kept.append(name)

print(kept)
print(len(files))  # 原清单仍有四项。
