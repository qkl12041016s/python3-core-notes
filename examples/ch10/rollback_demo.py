from contextlib import closing
import sqlite3

with closing(sqlite3.connect(":memory:")) as db:
    db.execute("CREATE TABLE notes (name TEXT)")
    try:
        with db:
            db.execute(
                "INSERT INTO notes VALUES (?)",
                ("notes.md",),
            )
            raise ValueError("取消本次写入")
    except ValueError:
        # 事务块离开时已回滚，再查一次。
        count = db.execute(
            "SELECT count(*) FROM notes"
        ).fetchone()[0]
        print(count)
