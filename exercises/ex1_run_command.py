"""課題1: コマンドを実行して、標準出力を文字列で受け取ろう。

やること:
    run_command(["who"]) のように、コマンドをリストで渡すと、
    そのコマンドの標準出力(文字列)を返す関数を作る。

例:
    run_command(["echo", "hello"])  ->  "hello\\n"

確認方法:
    python exercises/ex1_run_command.py
    pytest tests/test_ex1.py
"""


def run_command(cmd):
    # TODO: ここを自分で書く(README のヒントは、悩んでから開こう)
    raise NotImplementedError("TODO: run_command を実装しよう")


if __name__ == "__main__":
    # ターミナルで `who` を実行した結果と同じになるか見比べよう
    print(run_command(["who"]), end="")
