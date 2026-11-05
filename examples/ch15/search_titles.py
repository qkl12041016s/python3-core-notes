def search_titles(titles, query):
    # 界面传来的输入先去空格，再统一比较大小写。
    key = query.strip().casefold()
    return [title for title in titles if key in title.casefold()]


# 没有窗口时也可以核对搜索结果。
if __name__ == "__main__":
    titles = ["notes.md", "todo.md", "old_notes.md"]
    print(search_titles(titles, " NOTES "))
