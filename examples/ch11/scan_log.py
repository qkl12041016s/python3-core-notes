import argparse
from datetime import datetime, timezone
from pathlib import Path
import re

# 只提取约定格式的时间字段和 IP 字段。
pattern = re.compile(r"^(\S+)\s+ip=(\S+)$")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    args = parser.parse_args()

    content = args.input.read_text(encoding="utf-8")
    for line in content.splitlines():
        match = pattern.fullmatch(line)
        if match is None:
            continue
        stamp, address = match.groups()
        moment = datetime.fromisoformat(stamp)
        utc_stamp = moment.astimezone(timezone.utc).isoformat()
        print(utc_stamp, address)


if __name__ == "__main__":
    main()
