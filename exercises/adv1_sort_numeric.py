"""発展A: sort -n を再現しよう。

数字の文字列のリストを、数値の大きさ順に並べた新しいリストで返す。
通常の sort では ["10", "9", "100"] は ["10", "100", "9"] になってしまう。

例:
    my_sort_numeric(["10", "9", "100"])  ->  ["9", "10", "100"]

確認方法: pytest tests/test_adv.py
"""


def my_sort_numeric(lines, reverse=False):
    # TODO: 並べ替えの「基準」だけを数値に変えるには?
    raise NotImplementedError("TODO")
