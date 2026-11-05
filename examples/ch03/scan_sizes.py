import logging

# 坏记录写日志，合格的大小另存。
logging.basicConfig(level=logging.WARNING, format="%(message)s")
sizes = []
for raw in ["12", "bad", "0", "8"]:
    try:
        size = int(raw)
    except ValueError:
        logging.warning("忽略无效大小 %r", raw)
        continue

    if size > 0:
        sizes.append(size)

print(sizes)
