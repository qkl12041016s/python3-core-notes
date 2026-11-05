"""从事件 CSV 或 XLSX 生成清洗表、汇总表和 PDF 图。"""
import argparse
from pathlib import Path
from tempfile import TemporaryDirectory

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


def make_report(source, output):
    suffix = source.suffix.lower()
    if suffix == ".csv":
        table = pd.read_csv(source)
    elif suffix == ".xlsx":
        # 使用工作簿的第一张表，与 CSV 共用后续校验。
        table = pd.read_excel(source, engine="openpyxl")
    else:
        raise ValueError("输入文件须为 .csv 或 .xlsx")
    required = {"event_id", "team", "seconds"}
    if not required <= set(table.columns):
        raise ValueError("缺少 event_id、team 或 seconds 列")
    if table["event_id"].isna().any():
        raise ValueError("event_id 不能为空")

    # 同一事件只留首条，无法转为数值的耗时留作缺失。
    cleaned = table.drop_duplicates("event_id").copy()
    cleaned["seconds"] = pd.to_numeric(cleaned["seconds"], errors="coerce")
    if (cleaned["seconds"] < 0).any():
        raise ValueError("耗时不能小于零")
    cleaned["team"] = cleaned["team"].fillna("unknown")
    summary = cleaned.groupby("team", as_index=False).agg(
        events=("event_id", "size"),
        valid=("seconds", "count"),
        total=("seconds", lambda values: values.sum(min_count=1)),
    )
    # 全部产物先写到同卷临时目录，完成后再发布新目录。
    if output.exists():
        raise FileExistsError("输出目录已经存在，请选择新目录")
    output.parent.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(dir=output.parent) as folder:
        staged = Path(folder)
        cleaned.to_csv(staged / "cleaned.csv", index=False)
        with pd.ExcelWriter(staged / "report.xlsx", engine="openpyxl") as writer:
            cleaned.to_excel(writer, sheet_name="Cleaned", index=False)
            summary.to_excel(writer, sheet_name="Summary", index=False)
        # 图只使用同一份汇总表，空值在导出表中保留。
        figure, axis = plt.subplots(figsize=(5, 3), layout="constrained")
        axis.bar(summary["team"], summary["total"].fillna(0))
        axis.set(xlabel="Team", ylabel="Seconds")
        figure.savefig(staged / "report.pdf")
        plt.close(figure)
        staged.replace(output)
    return len(table), len(cleaned)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    print(make_report(args.input, args.output))
