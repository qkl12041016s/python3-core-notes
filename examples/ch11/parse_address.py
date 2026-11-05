import ipaddress
import re

# 正则先找字段，合法性再交给 IP 解析器。
line = "at=2026-01-01T00:00:00Z ip=192.0.2.1"
match = re.search(r"ip=(?P<address>\S+)", line)
if match is not None:
    address = ipaddress.ip_address(match.group("address"))
    print(address)
