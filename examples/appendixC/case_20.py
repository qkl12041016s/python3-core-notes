# 修复版。
import sqlite3
from contextlib import closing

with closing(sqlite3.connect(":memory:")) as db:
    # 初始化后再读取同一数据库。
    db.execute("CREATE TABLE notes (name TEXT)")
    print(db.execute("SELECT count(*) FROM notes").fetchone()[0])
