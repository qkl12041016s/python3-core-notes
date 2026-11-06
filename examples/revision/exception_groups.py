def validate_all():
    problems = [ValueError("empty title"), TypeError("bad count")]
    raise ExceptionGroup("validation", problems)


if __name__ == "__main__":
    try:
        validate_all()
    except* ValueError as group:
        print("value errors:", len(group.exceptions))
    except* TypeError as group:
        print("type errors:", len(group.exceptions))
