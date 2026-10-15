"""発展D: grep を再現しよう。

pattern を含む行だけをリストで返す(正規表現は使わず、単純な部分一致でよい)。
ignore_case=True のときは大文字小文字を区別しない(grep -i 相当)。

例:
    my_grep("an", ["banana", "cherry", "Angle"])                    ->  ["banana"]
    my_grep("an", ["banana", "cherry", "Angle"], ignore_case=True)  ->  ["banana", "Angle"]

確認方法: pytest tests/test_adv.py
"""


def my_grep(pattern, lines, ignore_case=False):
    # TODO
    raise NotImplementedError("TODO")
