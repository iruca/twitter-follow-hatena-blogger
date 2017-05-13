# twitter-follow-hatena-blogger
A library to follow hatena-bloggers  using twitter API.
Twitterのツイート検索APIとフォローAPIを使用してはてなブロガーを見つけ出し、1人フォローします。

## 準備
ディレクトリにtoken.yamlを作成し、その中に
- consumer_key
- consumer_secre
- access_token
- access_token_secret

を入力してください。
それぞれのtoken値は、
http://www.iruca21.com/entry/2017/05/13/140008
を参考に取得してください。

## 使い方
```
[root@hoge]# python follow_hatena_blogger.py
successfully followed 807806453071233024
```

実行成功すると、フォローしたユーザのuser IDが出力されます。
失敗した場合はマシンのネットワーク接続やtoken値を見直してください。
