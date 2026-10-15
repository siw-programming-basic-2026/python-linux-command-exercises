from ex3_sort import my_sort


def test_ascending():
    assert my_sort(["bob", "alice", "carol"]) == ["alice", "bob", "carol"]


def test_reverse():
    assert my_sort(["bob", "alice", "carol"], reverse=True) == ["carol", "bob", "alice"]


def test_does_not_modify_input():
    data = ["b", "a"]
    my_sort(data)
    assert data == ["b", "a"]


def test_returns_list_and_empty():
    assert my_sort([]) == []


def test_uppercase_before_lowercase():
    assert my_sort(["a", "B"]) == ["B", "a"]
