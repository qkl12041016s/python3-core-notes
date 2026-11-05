# 修复版。
# 空输入对应没有平均值这一状态。
values = []
average = sum(values) / len(values) if values else None
print(average)
