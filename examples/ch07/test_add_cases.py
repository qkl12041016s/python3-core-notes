import pytest


def add(left, right):
    # 被测函数保持明确的输入与输出。
    return left + right


@pytest.mark.parametrize(
    "left,right,expected",
    [(2, 3, 5), (-2, 3, 1), (0, 0, 0)],
)
def test_add(left, right, expected):
    assert add(left, right) == expected
