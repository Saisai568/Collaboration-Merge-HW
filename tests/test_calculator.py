# tests/test_calculator.py

from src.calculator import add, subtract


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 5) == 5


# 故意留下一個失敗的測試 (用於 pytest)
def test_add_negative_bug():
    # 這個 assert 應該是 -2，但我們故意寫 -3
    assert add(-1, -1) == -2
