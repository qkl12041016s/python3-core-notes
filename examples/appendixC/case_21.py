# 修复版。
import sqlite3
from contextlib import closing

with closing(sqlite3.connect(":memory:")) as db, db:
    db.execute("CREATE TABLE notes (name TEXT UNIQUE)")
    # 本例约定同名重试保留原记录。
    for _ in range(2):
        db.execute("INSERT OR IGNORE INTO notes VALUES (?)", ("notes.md",))
    print(db.execute("SELECT count(*) FROM notes").fetchone()[0])
