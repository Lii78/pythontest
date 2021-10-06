import sys
#args = sys.args
import os
import random
import requests #通信用のライブラリ
import re

def test(file):
    print(file)

file='b'
test(file)

url = 'https://news.yahoo.co.jp'
response = requests.get(url)
print(response.text[:5])
#print(response.status_code)
#レスポンスヘッダ（キーと値のペア）を取得
#for key,value in response.headers.items():
#    print(key,' ',value)
print(response.encoding)

s="あなたとわたし"
m=re.match("あな", s)
print(m.group())
#random.
print(os.getcwd())
#os.mkdir('./tester')
os.chdir('./tester')
print(os.getcwd())
print('a')
sys.exit()
x=10
print('b')
