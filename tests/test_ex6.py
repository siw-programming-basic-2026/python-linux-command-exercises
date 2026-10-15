from ex6_pipeline import login_ranking


def test_sample(who_sample):
    assert login_ranking(who_sample) == [(3, "alice"), (2, "bob"), (1, "carol")]


def test_tie_sorted_by_name():
    text = "zed pts/0\namy pts/1\n"
    assert login_ranking(text) == [(1, "amy"), (1, "zed")]


def test_unsorted_input_is_counted_together():
    text = "bob pts/0\nalice pts/1\nbob pts/2\n"
    assert login_ranking(text) == [(2, "bob"), (1, "alice")]


def test_empty():
    assert login_ranking("") == []
