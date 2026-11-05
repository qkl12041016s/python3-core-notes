class Job:
    def label(self):
        return "sync"


class NamedJob(Job):
    def label(self):
        # super 取父层行为，再补当前层的信息。
        return super().label() + ":notes.md"


print(NamedJob().label())
print([cls.__name__ for cls in NamedJob.__mro__])
