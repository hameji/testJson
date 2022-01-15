# pip install dataclasses が必要! (python 3.7 から導入された、それ以前のversionでは使えない )

from dataclasses import dataclass

# @dataclass をクラスの前につけて、型を宣言する
@dataclass
class Book:
    title: str
    year: int
    page: int

# 通常はこのようにデータを与え、初期化する(インスタンス化する)
python_book = Book(title="Python Beginners", year=2005, page=399)

print(" Book: ", python_book)

# 利点は、
# python_book. と打ち込むと、
# オートコンプリートで、要素(プロパティ)の
# title, page, year が自動で選択肢として表示されるようになる。 

print(f" title: " + python_book.title)

print(f" year: {python_book.year}")
print(f" page: {python_book.page}")

# 補足
# print文は、title のように + もしくは , で接続できますが、
# year, pageのように、f" "　とすることで、 { } で囲むことにより、文字列の中に直接 変数をかけるようになる
# 読みやすく、短くかけるので、こっちの方が好まれる。特に変数が増えると、f"" の方が楽

# 課題4-1
# 「book: XXXX, year: XXXX, page: XXXX」 とprint文で2つの方法で、出力してみましょう

  
fruit_grape = {
    "name": "ぶどう",
    "color": "紫色",
    "price": 100
}

# 課題4-2
# 上記 fruit_grape 用にdataclassを作成し、値をセットしたインスタンスを作ろう。

