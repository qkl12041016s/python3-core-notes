"""资料索引的持久化层，界面和 API 共用。"""
from contextlib import closing
from pathlib import Path
import sqlite3


class Library:
    def __init__(self, database):
        self.database = Path(database)
        self.database.parent.mkdir(parents=True, exist_ok=True)
        with closing(self.connect()) as db, db:
            db.execute(
                "CREATE TABLE IF NOT EXISTS notes "
                "(id INTEGER PRIMARY KEY, title TEXT NOT NULL, path TEXT UNIQUE NOT NULL)"
            )

    def connect(self):
        # 每次操作各开连接，适用于 API 的不同工作线程。
        db = sqlite3.connect(self.database)
        db.row_factory = sqlite3.Row
        return db

    def add(self, title, path):
        title, path = title.strip(), path.strip()
        if not title or not path:
            raise ValueError("标题和路径不能为空")
        with closing(self.connect()) as db, db:
            cursor = db.execute(
                "INSERT INTO notes(title, path) VALUES (?, ?)", (title, path)
            )
            return cursor.lastrowid

    def get(self, note_id):
        with closing(self.connect()) as db:
            row = db.execute("SELECT * FROM notes WHERE id = ?", (note_id,)).fetchone()
            return dict(row) if row is not None else None

    def search(self, query=""):
        with closing(self.connect()) as db:
            # instr 将查询词按字面匹配，避免把百分号当通配符。
            rows = db.execute(
                "SELECT * FROM notes WHERE instr(title, ?) > 0 ORDER BY id", (query,)
            ).fetchall()
            return [dict(row) for row in rows]
