# effecounter

## effecounter 構想
effectiveness counter の略で、Engineering Effectiveness の考え方に則っている。最大の生産性を出せる「集中しやすい状態」を理想とし、この理想を長くキープできれば良いとの前提のもと、この理想を阻む因子を計測する。より抽象化すれば、理想状態を阻む因子を計測する。

effecounter では、因子をシンプルに計測することに特化する。

```
python effecounter.py --label "dac"
```

これを実行すると、effecounter.md に次の形で保存する。logs の部分に append している。

```
# labels
- dac: Disagree and Commit したとき

# logs
- 2026/05/10 05:12:14 dac: 
- 2026/05/10 05:49:56 dac: テックリードとスクラムマスターは視座が低くて通じないことがわかった

```

なお、effecounter 起動時は一行入力ボックスを表示し、コメントを入力できる。空で提出 or esc キーなどでキャンセルした場合は、コメントは無しとみなす（05:12:14 の例はコメント無しなので何も書いてない）。

labels は事前に入力しておく必要があり、見当たらない場合はエラーとみなして、以下 open log を実行せよ。

特殊操作:

- open log: effecounter.md を関連付けで開く。入力ボックスでは `/` を提出することでも呼び出せる
