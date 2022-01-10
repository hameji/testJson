import json

## jsonファイルの読み込み
json_file1 = open('test1.json', 'r')
json_dic_data = json.load(json_file1)

## ファイルの中身の確認
print(json_dic_data)

## いよいよjsonからデータを取り出してみよう

# 課題2-1　book2のページ数を取得してみよう



