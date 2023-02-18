import requests
import urllib
import pandas as pd
#広域防災拠点csv




#国土地理院API
'''
Address = "愛媛県宇和島市吉田町立間尻 甲495−7"
makeUrl = "https://msearch.gsi.go.jp/address-search/AddressSearch?q="
s_quote = urllib.parse.quote(Address)
response = response = requests.get(makeUrl + s_quote)
print(response.json()[0]["geometry"]["coordinates"][0])
print(response.json()[0]["geometry"]["coordinates"][1])
'''

X = pd.read_excel('youshiki1-hinanbasyo (1).xlsx',header=None,names=['名称','住所','管理者電話','指定緊急避難場所との重複','福祉避難所','想定収容人数',],skiprows=4,usecols = "B:G")
X=X.replace({'指定緊急避難場所との重複': {1: '〇'}})
X=X.replace('\n', '')
#X=X.replace('\n', '', regex=True)
X=X.fillna('なし')
X=X.assign(緯度=0,経度=0)
index=435
Address = '愛媛県松山市南江戸4丁目1'
makeUrl = "https://msearch.gsi.go.jp/address-search/AddressSearch?q="
s_quote = urllib.parse.quote(Address)
response = response = requests.get(makeUrl + s_quote)

print('-------------------------------')
print('ここまではおけ')
print(index)
print(X.loc[index,'名称'])
print(X.loc[index,'住所'])
print(X.loc[index,'緯度'])
print(response.json())

X.loc[index,'緯度']=response.json()[0]["geometry"]["coordinates"][1]
X.loc[index,'経度']=response.json()[0]["geometry"]["coordinates"][0]
print(X.loc[index,'緯度'])
print(X.loc[index,'経度'])