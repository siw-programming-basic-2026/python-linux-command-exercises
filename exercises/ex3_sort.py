"""課題3: sort を再現しよう。

文字列のリストを受け取り、昇順に並べた「新しいリスト」を返す。
reverse=True のときは降順(sort -r 相当)。
元のリストを書き換えてはいけない。

例:
    my_sort(["bob", "alice", "carol"])  ->  ["alice", "bob", "carol"]

確認方法:
    python exercises/ex3_sort.py   (本物の sort と見比べる)
    pytest tests/test_ex3.py
"""
from compare import SAMPLE_WHO, real, show
from ex2_usernames import get_usernames


def my_sort(lines, reverse=False):
    # TODO: 標準の仕組みで並べ替える。どの関数を使えば元のリストが変わらない?
    raise NotImplementedError("TODO: my_sort を実装しよう")


if __name__ == "__main__":
    names = get_usernames(SAMPLE_WHO)
    text = "\n".join(names) + "\n"
    mine = "\n".join(my_sort(names)) + "\n"
    show("sort", real(["sort"], text), mine)
