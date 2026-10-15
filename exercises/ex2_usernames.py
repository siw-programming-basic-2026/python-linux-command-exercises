"""課題2: who の出力からユーザー名だけを取り出そう。(awk '{print $1}' 相当)

who の出力は 1行が「ユーザー名  端末  日付 時刻 (接続元)」の形をしている。
各行の先頭のユーザー名だけを、出てきた順にリストで返す関数を作る。

例:
    get_usernames("alice pts/0 2026-10-13 09:01\\nbob pts/1 2026-10-13 09:05\\n")
    ->  ["alice", "bob"]

注意: 空行があってもエラーにならないようにすること。
確認方法: pytest tests/test_ex2.py
"""
from compare import SAMPLE_WHO


def get_usernames(text):
    # TODO: 文字列を行ごとに分け、各行を空白で分けて先頭を取り出す
    raise NotImplementedError("TODO: get_usernames を実装しよう")


if __name__ == "__main__":
    print(get_usernames(SAMPLE_WHO))
