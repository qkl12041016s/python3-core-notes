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

    for line in args.input.read_text(encoding="utf-8").splitlines():
        match = pattern.fullmatch(line)
        if match is None:
            continue
        stamp, address = match.groups()
        moment = datetime.fromisoformat(stamp)
        print(moment.astimezone(timezone.utc).isoformat(), address)


if __name__ == "__main__":
    main()
