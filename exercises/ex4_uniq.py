"""課題4: uniq -c を再現しよう。

文字列のリストを受け取り、「隣り合う同じ行」をまとめて (回数, 行) のタプルのリストで返す。
本物の uniq と同じく、離れた場所にある同じ行は別々に数える。

例:
    my_uniq_count(["a", "a", "b", "a"])  ->  [(2, "a"), (1, "b"), (1, "a")]
    my_uniq_count([])                    ->  []

確認方法:
    python exercises/ex4_uniq.py   (本物の uniq -c と見比べる)
    pytest tests/test_ex4.py
"""
from compare import real, show


def my_uniq_count(lines):
    # TODO: 「直前の行と同じか?」で場合分けする。結果リストの最後の要素をどう使う?
    raise NotImplementedError("TODO: my_uniq_count を実装しよう")


if __name__ == "__main__":
    lines = ["alice", "alice", "bob", "alice"]
    text = "\n".join(lines) + "\n"
    mine = "".join(f"{n:7d} {s}\n" for n, s in my_uniq_count(lines))
    show("uniq -c", real(["uniq", "-c"], text), mine)
