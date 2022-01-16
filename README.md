# testJson

python における <br>

- 配列・辞書の扱い
- dataclass
- json, dataclasses_json

に慣れよう！ <br>

基本文法 <br>
https://qiita.com/motoki1990/items/74d850d2aaa5e19b65f1 <br>

# 課題１

配列・辞書から値を取り出す <br>
`task1.py` <br>

# 課題２

json ファイルを読み取り 1 <br>
`task2.py` <br>

# 課題 3

json ファイルの読み取り 2 <br>
`task3.py` <br>

# 発展

dataclass、dataclassJson を使おう <br>

これまでは json ( list もしくは dict ) をそのままその都度分解していました。 <br>
しかし、それでは、分解するごとにどうなっていたっけ？って毎回中身を確認する手間があったり、<br>
誤ってキー data['author'] のようにない項目にアクセスをしてしまい <br>
エラーを発生させてしまう懸念があります。 <br>

そこで、data を表すクラスを作って、それを利用することにより <br>
エラーの可能性を減らし(堅牢性:間違いの起こりにくい)、<br>
可読性(コードの読みやすさ)をあげることができます。 <br>

https://horomary.hatenablog.com/entry/2019/11/24/033557 <br>

# 課題 4

dataclass の使い方を見てみましょう <br>

`test4.py` <br>

# 課題 5

dataclassJson を使ってみよう <br>
では、簡単な json の値を dataclass に変換してみましょう <br>

`python5.py` <br>

# 課題 6

辞書・配列が複合的なデータを dataclass, dataclass_json を使ってデコードしよう<br>

`python6.py` <br>
