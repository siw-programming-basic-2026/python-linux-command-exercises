from ex2_usernames import get_usernames


def test_sample(who_sample):
    assert get_usernames(who_sample) == ["alice", "bob", "alice", "carol", "bob", "alice"]


def test_empty():
    assert get_usernames("") == []


def test_blank_lines_ignored():
    assert get_usernames("alice pts/0\n\n  \nbob pts/1\n") == ["alice", "bob"]
