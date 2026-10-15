"""本物のLinuxコマンドの出力を取得して、自作関数の結果と見比べるための補助ツール。

課題の答えは含まれていません。各課題ファイルの末尾から使われます。
"""
import subprocess

SAMPLE_WHO = """\
alice    pts/0        2026-10-13 09:01 (192.168.1.5)
bob      pts/1        2026-10-13 09:05 (192.168.1.7)
alice    pts/2        2026-10-13 09:10 (192.168.1.5)
carol    tty1         2026-10-13 08:55
bob      pts/3        2026-10-13 09:20 (192.168.1.7)
alice    pts/4        2026-10-13 09:30 (192.168.1.5)
"""


def real(cmd, text):
    """cmd を実行し、text を標準入力として渡したときの出力を返す(ロケールはC固定)。"""
    result = subprocess.run(
        cmd,
        input=text,
        capture_output=True,
        text=True,
        env={"LC_ALL": "C", "PATH": "/usr/bin:/bin"},
    )
    return result.stdout


def show(title, real_output, mine):
    """本物と自作の結果を並べて表示し、一致したかを知らせる。"""
    print(f"--- {title}: 本物のコマンド ---")
    print(real_output, end="" if real_output.endswith("\n") else "\n")
    print(f"--- {title}: 自作 ---")
    print(mine, end="" if str(mine).endswith("\n") else "\n")
    print("一致!" if str(real_output).split() == str(mine).split() else "違いがあります。見比べてみよう")
