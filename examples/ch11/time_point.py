from datetime import datetime, timedelta, timezone

# 同一时刻，分别显示 UTC 与固定的东八区偏移。
utc = datetime(2026, 1, 1, tzinfo=timezone.utc)
local = utc.astimezone(timezone(timedelta(hours=8)))
print(utc.isoformat())
print(local.isoformat())
print(utc.timestamp() == local.timestamp())
