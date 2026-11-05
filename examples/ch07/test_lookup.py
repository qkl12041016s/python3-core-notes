from unittest.mock import Mock


def lookup_status(fetch, filename):
    # fetch 由调用方提供，结果仍按正常业务结构读取。
    return fetch(filename)["status"]


def test_lookup():
    fetch = Mock(return_value={"status": "done"})
    assert lookup_status(fetch, "notes.md") == "done"
    fetch.assert_called_once_with("notes.md")


# 当作脚本运行时，可以直接核对这条测试。
if __name__ == "__main__":
    test_lookup()
    print("test_lookup passed")
