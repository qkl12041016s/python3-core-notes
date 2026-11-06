def describe(value: int | str | dict) -> str:
    match value:
        case bool():
            return "boolean"
        case int() as number if number >= 0:
            return f"nonnegative: {number}"
        case {"kind": "note", "title": str() as title}:
            return f"note: {title}"
        case str() as text:
            return text.strip()
        case _:
            return "unsupported"


if __name__ == "__main__":
    print(describe(7))
    print(describe({"kind": "note", "title": "Calculus"}))
    print(describe(True))
