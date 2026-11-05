def describe(name, *tags, enabled=True, **options):
    # args 收成元组，kwargs 收成字典。
    return name, tags, enabled, options.get("retries", 0)


result = describe(
    "sync", "daily", "local", enabled=False, retries=2
)
print(result)
