from contextlib import closing
import sqlite3

with closing(sqlite3.connect(":memory:")) as db:
    # 用带撇号的文件名核对绑定行为。
    name = "O'Brien.md"
    db.execute("CREATE TABLE files (name TEXT)")
    db.execute("INSERT INTO files VALUES (?)", (name,))

    # 语句结构和用户输入分别交给驱动。
    row = db.execute(
        "SELECT name FROM files WHERE name = ?", (name,)
    ).fetchone()
    print(row[0])
