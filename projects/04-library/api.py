"""本地 FastAPI 服务，启动命令见 README。"""
from pathlib import Path
import sqlite3

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator

from storage import Library


class NoteInput(BaseModel):
    title: str
    path: str

    @field_validator("title", "path")
    @classmethod
    def require_text(cls, value):
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("字段不能为空")
        return cleaned


def create_app(database=Path("library.sqlite")):
    library = Library(database)
    app = FastAPI()

    @app.post("/notes", status_code=201)
    def add_note(note: NoteInput):
        try:
            note_id = library.add(note.title, note.path)
        except sqlite3.IntegrityError as error:
            raise HTTPException(409, "路径已登记") from error
        return library.get(note_id)

    @app.get("/notes")
    def search_notes(query: str = ""):
        return library.search(query)

    @app.get("/notes/{note_id}")
    def get_note(note_id: int):
        note = library.get(note_id)
        if note is None:
            raise HTTPException(404, "资料不存在")
        return note

    return app
