import json
from dataclasses import dataclass
from dataclasses_json import dataclass_json

# 課題6
# dataclass, dataclass_json を使いこなそう
# 辞書(dict型)は 課題5 で理解できたと思います。
# 次は配列も混ざったものを分解してみましょう

# test2.json をDecodableBookに分解してみましょう

# このように書くことで、他のファイルの中身(クラスなど)を持ってこれる
from task5 import DecodableBook

print(f" ============================== ")
print(f" 課題6 ")
print(f" ============================== ")

json_file3 = open('test2.json', 'r')
json_data = json.load(json_file3)
json_str = json.dumps(json_data) 

print(f" data is {json_str}")

from typing import List # Python3.6 以降をサポート
# Python 3.7以降のみにしたい場合、上記ではなく、下記の行で
# from __future__ import annotations
# Python 3.9 以降であれば、上記どれも不要

# @dataclass_json, dataclass の書き方はこの順番じゃなきゃダメです。
@dataclass_json
@dataclass
class DecodableBooks:
    books: List[DecodableBook]
    
# 気づいたかもしれませんが、jsonのkey名とプロパティ名は合わせないといけないです。
    
books_from_json = DecodableBooks.from_json(json_str)
print(f" decoded data: {books_from_json}")
print(f" ============================== ")

# 中の要素は配列なので、下記のように取り出せます。
print(f" books: {books_from_json.books}")
print(f" ============================== ")
print(f" books [1] title: {books_from_json.books[1].title}")
print(f" ============================== ")


## 課題6-1
# test5.json を dataclass, dataclass_jsonを使って、クラスでしよう。
