#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
import urllib
import requests

list=[435, 494, 506, 545]

X=pd.read_csv('災害csv/指定緊急避難所一覧2x.csv')
#X=pd.read_csv('災害csv/活動拠点候補一覧.csv')

'''
#Address = X.loc[index,'住所']
Address = '愛媛県松山市余戸中5-3'
makeUrl = "https://msearch.gsi.go.jp/address-search/AddressSearch?q="
s_quote = urllib.parse.quote(Address)
response = response = requests.get(makeUrl + s_quote)
'''

X.loc[435,'緯度']=33.83744325
X.loc[435,'経度']=132.74269232
X.loc[494,'緯度']=33.86466762
X.loc[494,'経度']=132.72376994
X.loc[506,'緯度']=33.86871002
X.loc[506,'経度']=132.71542742
X.loc[545,'緯度']=33.81633733
X.loc[545,'経度']=132.73208659
for i in list:
 print('-------------------------------')
 print(X.loc[i,'名称'])
 print(X.loc[i,'緯度'])
 print(X.loc[i,'経度'])
 i
'''
print(response.json())

X.loc[index,'緯度']=response.json()[0]["geometry"]["coordinates"][1]
X.loc[index,'経度']=response.json()[0]["geometry"]["coordinates"][0]
print(X.loc[index,'緯度'])
print(X.loc[index,'経度'])
'''
#X=X.replace('\n', '',)
X.to_csv('災害csv/指定緊急避難所一覧2.csv')