# 14.1, 14.2, 14.4
import base64
from urllib import request
from urllib import parse

# 14.1 URL
# URLをパース
result = parse.urlparse(
    'https://www.example.com/test/;parameter?q=example#hoge')
print(result)  # パースの結果を返す
print(result.geturl())  # パース結果からURLを取得
print(result.scheme)  # タプルの要素に名前でアクセス
print(result[0])
print(result.hostname)  # タプルの要素以外にもいくつかの属性がある

print('---------------')

for i in range(len(result)):
    print(result[i])


# クエリ文字列をパース
'''
parse_qs()は「?」マーク以降をクエリ文字列としてパースする

parse_qs()はパースした結果をdictとして返す
parse_qsl()を使うとtupleで返すことができる
'''

result = parse.urlparse(
    'https://www.google.com/search?q=python&oq=python&sourceid=chrome&ie=UTF-8')
print(result.query)
print(parse.parse_qs(result.query))  # パース結果を辞書として受け取る
print(parse.parse_qsl(result.query))  # パース結果をタプルのリストとして受け取る

# クエリ文字列を組み立てる - urlencode()
print(parse.urlencode({'key1': 1, 'key2': 2, 'key3': 'ぱいそん'}))
print(parse.urlencode([('key1', 1), ('key2', 2), ('key3', 'パイソン')]))

query = {'key1': 'hoge', 'key2': ['foo', 'bar']}
print(parse.urlencode(query))
print(parse.urlencode(query, doseq=True))


# urlを開く - urllib.request

# GETメソッド
with request.urlopen('https://httpbin.org/get') as f:
    res = f.read()[:92]
print(res)

# ファイルのダウンロード
file_data = request.urlopen('https://httpbin.org/image/jpeg').read()

with open('./test.jpeg', 'wb') as f:
    f.write(file_data)

#　POSTメソッド
data = 'key1=value1&key2=value2'
res = request.urlopen('https://httpbin.org/post', data=data.encode())
print(res.status)

# DELETEメソッド
data = 'key1=value1&key2=value2'
req = request.Request('https://httpbin.org/delete',
                      data=data.encode(), method='DELETE')

with request.urlopen(req) as f:
    res_body = f.read()[:110]
    res_status = f.status

print(res_status)
print(res_body)

# カスタムヘッダーを設定
headers = {'Accept': 'application/json'}
print(request.Request('https://httpbin.org/get', headers=headers))

# レスポンスモジュール
res = request.urlopen('https://httpbin.org/get')
print(res.url)
print(res.status)
print(res.headers)


# Base16, Base63などへエンコードする - base64
'''
base64モジュールは、データのエンコードおよびデコードを扱う

base64モジュールは以下のエンコード方式を扱うことができる

Base16
Base32
Base64
Base84
'''

# Base64にエンコード
s = 'Pythonは簡単に習得でき、それでいて強力な言語の１つです。'
# base64.b64encode(s)  文字列を渡すとエラーになる
print(base64.b64encode(s.encode()))  # バイト文字列にエンコードして返す

# Base64からデコードする
enc_s = base64.b64encode(s.encode())
print(base64.b64decode(enc_s).decode())
