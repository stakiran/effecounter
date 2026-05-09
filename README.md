[日本語](README.md) | [English](README_en.md)

# effecounter
理想状態を阻む因子を計測するカウンターアプリ。ラベルを指定して実行すると、タイムスタンプとコメント付きで `effecounter.md` に追記される。

effecounter は effectiveness counter の略で、engineering effectiveness の考え方を参考にしている。

## 使い方

```
python effecounter.py --label "dac"
```

※これは「Disagree and Commit を実行したとき」を記録するために、dac というラベルを使っている

実行すると一行入力ボックスが表示され、コメントを入力して Enter で記録（空でも可能）。Esc でキャンセル。`/` を提出すると `effecounter.md` を関連付けで開く。

ラベルは事前に `effecounter.md` の `# labels` セクションに記載しておく必要がある。未登録のラベルを指定した場合は自動で `effecounter.md` が開かれる。

## ライセンス

[LICENSE](LICENSE) を参照。
