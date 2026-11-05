import csv
import io

from bs4 import BeautifulSoup

html = """<table id="files">
<tr><th>name</th><th>status</th></tr>
<tr><td>notes.md</td><td>done</td></tr>
</table>"""
soup = BeautifulSoup(html, "html.parser")
stream = io.StringIO(newline="")
writer = csv.writer(stream, lineterminator="\n")

# 逐行提取，CSV 模块负责转义和分隔。
for row in soup.select("#files tr"):
    cells = row.select("th, td")
    writer.writerow([cell.get_text(strip=True) for cell in cells])

print(stream.getvalue(), end="")
