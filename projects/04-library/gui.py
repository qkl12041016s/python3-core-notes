"""PyQt6 本地资料管理界面。"""
from pathlib import Path
import sqlite3
import sys

from PyQt6.QtWidgets import (
    QApplication, QFileDialog, QLineEdit, QListWidget,
    QMessageBox, QPushButton, QVBoxLayout, QWidget,
)

from storage import Library


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.library = Library(Path("library.sqlite"))
        self.setWindowTitle("学习资料管理器")
        self.query = QLineEdit()
        self.query.setPlaceholderText("输入标题查询")
        self.results = QListWidget()
        add_button = QPushButton("登记文件")
        layout = QVBoxLayout(self)
        for widget in (self.query, add_button, self.results):
            layout.addWidget(widget)
        self.query.textChanged.connect(self.refresh)
        add_button.clicked.connect(self.add_file)
        self.refresh()

    def refresh(self):
        self.results.clear()
        for row in self.library.search(self.query.text()):
            self.results.addItem(f"{row['title']} | {row['path']}")

    def add_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "选择资料")
        if not filename:
            return
        path = Path(filename).resolve()
        try:
            self.library.add(path.name, str(path))
        except (ValueError, sqlite3.IntegrityError) as error:
            QMessageBox.warning(self, "登记失败", str(error))
        self.refresh()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
