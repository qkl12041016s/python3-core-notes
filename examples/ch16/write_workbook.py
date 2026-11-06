from pathlib import Path
from tempfile import TemporaryDirectory

from openpyxl import Workbook, load_workbook

with TemporaryDirectory() as folder:
    path = Path(folder) / "report.xlsx"
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Summary"
    sheet.append(["team", "files"])
    sheet.append(["A", 5])
    sheet.append(["B", 4])
    workbook.save(path)
    workbook.close()

    # 重新读文件，核对表头后的两行。
    restored = load_workbook(path, read_only=True)
    print(
        restored["Summary"].max_row,
        restored["Summary"]["B3"].value,
    )
    restored.close()
