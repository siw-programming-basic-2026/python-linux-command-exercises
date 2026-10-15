"""発展課題のテスト。取り組んだ課題の分だけ通ればよい。"""
from adv1_sort_numeric import my_sort_numeric
from adv2_counter import count_all
from adv3_grep import my_grep


def test_sort_numeric():
    assert my_sort_numeric(["10", "9", "100"]) == ["9", "10", "100"]
    assert my_sort_numeric(["10", "9", "100"], reverse=True) == ["100", "10", "9"]


def test_count_all_non_adjacent():
    assert count_all(["a", "b", "a"]) == [(2, "a"), (1, "b")]


def test_count_all_empty():
    assert count_all([]) == []


def test_grep():
    data = ["banana", "cherry", "Angle"]
    assert my_grep("an", data) == ["banana"]
    assert my_grep("an", data, ignore_case=True) == ["banana", "Angle"]
