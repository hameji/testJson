# pip install dataclasses_json が必要!
import json

from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class DecodableBook:
    title: str
    page: int
    year: int

# jsonファイルの読み込み
json_file3 = open('test3.json', 'r')
json_data = json.load(json_file3)

# 中身確認用
print(f" content of json file: {json_data}")
print(f" type is {type(json_data)}") # type(変数) とすることで、その変数のクラスを確認できます。

# dataclass_jsonで利用できるように、dict型 から str型 に変換
json_str = json.dumps(json_data) 

# DecodableBook の dataclassに変換 
# ( Decodable とはjson -> dataclass へデコード(変換)可能との意味 )
# 対義語は codable と言う dataclass -> jsonへコード(変換)
book_from_json = DecodableBook.from_json(json_str)
print(book_from_json)

# 課題5-1
# 同様に、test4.json (task4-2) でやったブドウのデータが入ってます
# をdataclassに変換してみましょう。