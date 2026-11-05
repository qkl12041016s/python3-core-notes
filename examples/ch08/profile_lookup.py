import cProfile
import pstats


def count_matches(files, queries):
    # 反复在列表里查名字，保留同一份输入。
    return sum(name in files for name in queries)


files = [f"file-{i}.md" for i in range(1000)]
queries = ["file-999.md", "missing.md"] * 1000
profiler = cProfile.Profile()
hits = profiler.runcall(count_matches, files, queries)
print("命中数", hits)

# 按累计耗时排序，显示前四条记录。
pstats.Stats(profiler).sort_stats("cumulative").print_stats(4)
