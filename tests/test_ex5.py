from ex5_wc import my_wc


def test_basic():
    assert my_wc("hello world\nfoo\n") == (2, 3, 16)


def test_no_trailing_newline():
    assert my_wc("a b") == (0, 2, 3)


def test_empty():
    assert my_wc("") == (0, 0, 0)


def test_multiple_spaces():
    assert my_wc("a   b\n") == (1, 2, 6)


def test_japanese_counts_characters():
    assert my_wc("こんにちは\n") == (1, 1, 6)
