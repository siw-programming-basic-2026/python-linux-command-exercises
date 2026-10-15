"""課題5: wc を再現しよう。

文字列を受け取り、(行数, 単語数, 文字数) のタプルを返す。
wc -l / -w / -m と同じ結果になること。

例:
    my_wc("hello world\\nfoo\\n")  ->  (2, 3, 16)
    my_wc("a b")                  ->  (0, 2, 3)    # 最後に改行がないと行数は増えない!

確認方法:
    python exercises/ex5_wc.py   (本物の wc と見比べる)
    pytest tests/test_ex5.py
"""
from compare import SAMPLE_WHO, real, show


def my_wc(text):
    # TODO: 行数は「何を数えると wc -l と一致する?」を実験して決めよう
    raise NotImplementedError("TODO: my_wc を実装しよう")


if __name__ == "__main__":
    lines, words, chars = my_wc(SAMPLE_WHO)
    mine = f"{lines} {words} {chars}"
    show("wc -lwm", real(["wc", "-l", "-w", "-m"], SAMPLE_WHO), mine)
