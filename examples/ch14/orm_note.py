from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    pass


class Note(Base):
    __tablename__ = "notes"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)


engine = create_engine("sqlite+pysqlite:///:memory:")
Base.metadata.create_all(engine)
# 提交后换一个会话读取。
with Session(engine) as session, session.begin():
    session.add(Note(name="notes.md"))
with Session(engine) as session:
    note = session.scalar(select(Note).where(Note.name == "notes.md"))
    print(note.name)
engine.dispose()
