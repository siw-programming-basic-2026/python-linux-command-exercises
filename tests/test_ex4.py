from ex4_uniq import my_uniq_count


def test_adjacent_duplicates():
    assert my_uniq_count(["a", "a", "b"]) == [(2, "a"), (1, "b")]


def test_non_adjacent_counted_separately():
    assert my_uniq_count(["a", "a", "b", "a"]) == [(2, "a"), (1, "b"), (1, "a")]


def test_empty():
    assert my_uniq_count([]) == []


def test_single():
    assert my_uniq_count(["x"]) == [(1, "x")]


def test_all_same():
    assert my_uniq_count(["x"] * 4) == [(4, "x")]
