"""課題6: これまでの部品をつないで「ログイン中ユーザーのランキング」を作ろう。

シェルでは次のように書ける:
    who | awk '{print $1}' | sort | uniq -c | sort -rn

login_ranking(who_text) は who の出力(文字列)を受け取り、
(回数, ユーザー名) のリストを「回数の多い順、同数ならユーザー名順」で返す。

例(compare.SAMPLE_WHO を渡した場合):
    [(3, "alice"), (2, "bob"), (1, "carol")]

自分で作った ex2〜ex4 の関数を import して使うこと。
確認方法:
    python exercises/ex6_pipeline.py --sample   (サンプルデータで実行)
    python exercises/ex6_pipeline.py            (本物の who で実行)
    pytest tests/test_ex6.py
"""
import sys

from compare import SAMPLE_WHO
from ex1_run_command import run_command
from ex2_usernames import get_usernames
from ex3_sort import my_sort
from ex4_uniq import my_uniq_count
from ex5_wc import my_wc


def login_ranking(who_text):
    # TODO: get_usernames -> my_sort -> my_uniq_count の順につなぎ、
    #       最後に回数の多い順に並べ替える(ヒント: sorted の key と、負の数)
    raise NotImplementedError("TODO: login_ranking を実装しよう")


def main():
    who_text = SAMPLE_WHO if "--sample" in sys.argv else run_command(["who"])
    for count, name in login_ranking(who_text):
        print(f"{count:7d} {name}")
    print(f"ログイン総数: {my_wc(who_text)[0]}")


if __name__ == "__main__":
    main()
