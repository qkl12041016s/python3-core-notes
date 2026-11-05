class Contact:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        # 日常显示用简洁名字。
        return self.name

    def __repr__(self):
        # 调试时保留类型名和字符串边界。
        return f"Contact(name={self.name!r})"


person = Contact("小雪")
print(person)
print(repr(person))
