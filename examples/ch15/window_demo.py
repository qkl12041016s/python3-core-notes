import tkinter as tk
from tkinter import ttk


def greet():
    # 回调只取输入并更新显示。
    text = entry.get().strip()
    result.set(f"你好，{text}" if text else "请先输入名字")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("笔记问候")
    entry = ttk.Entry(root)
    entry.pack(padx=16, pady=8)
    result = tk.StringVar(value="等待输入")
    ttk.Button(root, text="问候", command=greet).pack()
    ttk.Label(root, textvariable=result).pack(pady=8)
    root.mainloop()
