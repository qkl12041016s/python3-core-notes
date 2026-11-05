"""单用户命令行通讯录，用 JSON 保存记录。"""
import argparse
import json
import os
from pathlib import Path
from tempfile import NamedTemporaryFile


def read_contacts(path):
    # 只把文件不存在视作首次运行，格式错误继续报告。
    if not path.exists():
        return {}
    records = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(records, dict) or not all(
        isinstance(name, str) and isinstance(phone, str)
        for name, phone in records.items()
    ):
        raise ValueError("通讯录必须是姓名到电话的字典")
    return records


def write_contacts(path, records):
    # 临时文件与目标同目录，完整写好后再替换。
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=path.parent, delete=False
        ) as stream:
            temporary = Path(stream.name)
            json.dump(records, stream, ensure_ascii=False, indent=2)
            stream.flush()
            os.fsync(stream.fileno())
        temporary.replace(path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=Path, default=Path("contacts.json"))
    commands = parser.add_subparsers(dest="command", required=True)
    add = commands.add_parser("add")
    add.add_argument("name")
    add.add_argument("phone")
    update = commands.add_parser("update", help="修改已有联系人的电话")
    update.add_argument("name")
    update.add_argument("phone")
    commands.add_parser("list")
    remove = commands.add_parser("remove")
    remove.add_argument("name")
    args = parser.parse_args(argv)

    try:
        contacts = read_contacts(args.file)
        if args.command in {"add", "update"}:
            name, phone = args.name.strip(), args.phone.strip()
            if not name or not phone:
                raise ValueError("姓名和电话不能为空")
            if args.command == "add" and name in contacts:
                raise ValueError("姓名已存在")
            if args.command == "update" and name not in contacts:
                raise ValueError("联系人不存在")
            contacts[name] = phone
            write_contacts(args.file, contacts)
            print("已保存", name)
        elif args.command == "remove":
            if args.name not in contacts:
                raise ValueError("联系人不存在")
            del contacts[args.name]
            write_contacts(args.file, contacts)
            print("已删除", args.name)
        else:
            for name, phone in sorted(contacts.items()):
                print(name, phone)
    except (OSError, ValueError) as error:
        parser.exit(1, str(error) + "\n")


if __name__ == "__main__":
    main()
