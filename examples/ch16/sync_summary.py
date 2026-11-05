from io import StringIO

import pandas as pd

# 用带缺失值的小表核对统计口径。
sample = StringIO("team,seconds\nteam-a,2\nteam-a,\nteam-b,3\n")
table = pd.read_csv(sample)

# size 算行数，count 算有值的记录数。
summary = table.groupby("team", as_index=False).agg(
    rows=("seconds", "size"),
    valid=("seconds", "count"),
    total=("seconds", "sum"),
)
row = summary.loc[summary["team"] == "team-a"].iloc[0]
print(len(table), row["rows"], row["valid"], row["total"])
