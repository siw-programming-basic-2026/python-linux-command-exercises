# LinuxコマンドをPythonで作ってみよう(90分)

`who | awk '{print $1}' | sort | uniq -c | sort -rn` というシェルのパイプラインを、Pythonで一歩ずつ再現します。

## 学習目標

この授業が終わると、次のことができます。

1. Pythonから Linux コマンドを実行し、出力を文字列として受け取れる(`subprocess`)
2. コマンドは「入力 → 処理 → 出力」であり、パイプは出力を次の入力につなぐ仕組みだと説明できる
3. `sort` / `uniq -c` / `wc` の動作を、標準の機能で再現できる
4. 「コマンドを呼ぶ方法」と「Pythonで実装する方法」の長所・短所を比べて言える
5. `pytest` で自分のコードの正しさを確認できる

## 進め方

各課題は次の流れです。

1. **Linuxで試す**: ターミナルで本物のコマンドを動かし、動きを観察する
2. **自分で考える**: `exercises/` のファイルの `TODO` を自分で書く
3. **比べる**: `python exercises/exN_*.py` で本物と自作の出力を見比べる
4. **確かめる**: `pytest tests/test_exN.py` で確認する

凡例: 🧠 自分で考える / 📖 調べてよい / 💡 ヒント(悩んでから開く)

## 準備

```bash
cd 作成したリポジトリ名
python3 --version          # 3.10 以上
python3 -m pip install pytest
pytest                     # 最初は全部失敗します。これが出発点です
```

> `pytest` は `exercises/` をテストします。すべて失敗(`NotImplementedError`)から始まり、課題を進めるたびに緑(合格)が増えていきます。

## タイムテーブル

| 時間 | 内容 |
|---|---|
| 0-10分 | 導入: パイプラインを観察する |
| 10-25分 | 課題1: `who` をPythonから実行する |
| 25-45分 | 課題2・3: ユーザー名の取り出しと `sort` |
| 45-60分 | 課題4・5: `uniq -c` と `wc` |
| 60-65分 | 休憩・中間確認 |
| 65-80分 | 課題6: パイプラインの完成 |
| 80-90分 | 比較と振り返り |

## 導入: パイプラインを観察しよう(0-10分)

ターミナルで、1行ずつ `|` を足しながら実行し、出力がどう変わるか観察します。

```bash
who
who | awk '{print $1}'
who | awk '{print $1}' | sort
who | awk '{print $1}' | sort | uniq -c
who | awk '{print $1}' | sort | uniq -c | sort -rn
who | wc -l
```

🧠 考えてみよう: 各段階で「入力は何か、出力は何か」。`sort` を省いて `uniq -c` だけにするとどうなるか。

> ログイン中のユーザーが自分だけなら、`ssh` や複数ターミナルで同じユーザーのログインを増やすと違いが見えます。
> 結果が少ないときは `exercises/compare.py` の `SAMPLE_WHO`(サンプルデータ)を使います。

## 基礎課題

### 課題1: コマンドを実行する(`ex1_run_command.py`)

`run_command(["who"])` で `who` の出力を文字列として受け取る関数を作ります。

🧠 コマンドの実行結果をPythonの変数に入れるには、どうすればよいでしょう? 
📖 調べてよい: Python公式ドキュメントの「subprocess」

<details><summary>💡 ヒント1(方向性)</summary>

標準ライブラリの `subprocess` モジュールにコマンドを実行する関数があります。
</details>
<details><summary>💡 ヒント2(使う関数)</summary>

`subprocess.run(...)` を使います。出力を受け取るには `capture_output=True`、バイト列でなく文字列にするには `text=True` を指定します。戻り値のオブジェクトの `.stdout` が出力です。
</details>
<details><summary>💡 ヒント3(小さな例)</summary>

```python
import subprocess
r = subprocess.run(["echo", "hi"], capture_output=True, text=True)
print(repr(r.stdout))
```
</details>

### 課題2: ユーザー名を取り出す(`ex2_usernames.py`)

`awk '{print $1}'` の代わりに、`who` の出力から各行の先頭(ユーザー名)をリストにします。

🧠 文字列を「行」に、行を「単語」に分けるには?空行が来たらどうなる?

<details><summary>💡 ヒント1</summary>文字列には、行や単語に分ける便利なメソッドがあります。</details>
<details><summary>💡 ヒント2</summary><code>splitlines()</code> と <code>split()</code> を使います。空行を <code>split()</code> すると空リストになることに注意。</details>
<details><summary>💡 ヒント3</summary>

```python
"alice  pts/0  09:01".split()   # ['alice', 'pts/0', '09:01']
"".split()                      # []
```
</details>

### 課題3: `sort` を再現する(`ex3_sort.py`)

文字列のリストを昇順に並べた**新しいリスト**を返します。`reverse=True` なら降順(`sort -r`)。

🧠 `list.sort()` と `sorted()` の違いは?元のリストが変わっていいのはどちら?
`python exercises/ex3_sort.py` で本物の `sort` と比べましょう。

<details><summary>💡 ヒント</summary><code>sorted(リスト, reverse=...)</code> は新しいリストを返し、元を変更しません。</details>

### 課題4: `uniq -c` を再現する(`ex4_uniq.py`)

隣り合う同じ行をまとめ、`(回数, 行)` のリストを返します。

🧠 まず本物で `printf 'a\na\nb\na\n' | uniq -c` を実行し、最後の `a` がどう扱われるか確認しましょう。なぜ `uniq` の前に `sort` が必要なのでしょう?

<details><summary>💡 ヒント1</summary>for で1行ずつ見て「直前の行と同じか」で場合分けします。</details>
<details><summary>💡 ヒント2</summary>結果のリストの最後の要素は <code>result[-1]</code> で取れます。タプルは書き換えられないので、作り直します。</details>
<details><summary>💡 ヒント3</summary>結果が空のうちは <code>result[-1]</code> が使えません。<code>if result and ...</code> の形を考えてみよう。</details>

### 課題5: `wc` を再現する(`ex5_wc.py`)

文字列から `(行数, 単語数, 文字数)` を返します。

🧠 `printf 'a b' | wc -l` の結果は何?(実際に試すこと)行数は「何を数えると」一致するでしょう?

<details><summary>💡 ヒント1</summary><code>wc -l</code> は改行文字の数を数えています。</details>
<details><summary>💡 ヒント2</summary>文字列の <code>count()</code> メソッド、<code>split()</code>、<code>len()</code> が使えます。</details>

### 課題6: パイプラインを完成させる(`ex6_pipeline.py`)

課題2〜4の関数をつなぎ、ログインユーザーのランキングを作ります。

```bash
python exercises/ex6_pipeline.py --sample    # サンプルで確認
python exercises/ex6_pipeline.py             # 本物の who で実行
```

🧠 自作した関数を `import` して部品として組み合わせます。最後の `sort -rn` に相当する「回数の多い順」はどう作る?

<details><summary>💡 ヒント1</summary><code>sorted(..., key=関数)</code> で並べ替えの基準を指定できます。</details>
<details><summary>💡 ヒント2</summary>タプル <code>(-回数, 名前)</code> を key にすると「回数の多い順、同数なら名前順」になります。</details>

## 振り返り(80-90分)

ペアまたは個人で、次を言葉にしましょう。

| | `subprocess` で `sort` を呼ぶ | Pythonで自作する |
|---|---|---|
| 手軽さ | | |
| 環境への依存(Windowsでは?) | | |
| 動作の細かい制御 | | |
| 速度・巨大データ | | |

- 本物と自作で結果が違った場面はあったか。なぜか。
- `sort` の結果が環境(ロケール)で変わる可能性はあるか。

## 発展課題(任意)

- **A**: `adv1_sort_numeric.py` — `sort -n`。なぜ文字列のままだと `100` が `9` より前に来る?
- **B**: `adv2_counter.py` — `collections.Counter` で数える。`sort | uniq -c` との違いは?
- **C**: ex6 を `argparse` でオプション化し、標準入力(`sys.stdin`)から読めるようにする。`who | python ex6_pipeline.py` と書けるか?
- **D**: `adv3_grep.py` — `grep` / `grep -i`。

発展A・B・Dは `pytest tests/test_adv.py` で確認できます。

## ディレクトリ構成

```
README.md           この資料
exercises/          学生が編集する課題(compare.py は比較用の補助。編集不要)
tests/              pytest による確認
pytest.ini          pytestの設定
```
