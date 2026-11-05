class SyncJob:
    def __init__(self, name):
        self.name = name
        # 每个实例在初始化时建自己的日志。
        self.log = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("任务名不能为空")
        self._name = cleaned


# 给一个实例写日志，再检查另一个实例。
first = SyncJob(" notes.md ")
second = SyncJob("todo.md")
first.log.append("queued")
print(first.name, first.log)
print(second.name, second.log)
