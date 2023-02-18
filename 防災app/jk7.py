#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
import urllib
import requests

#物資集積所
X = pd.read_excel('03youryou-shiryou3.xlsx',header=None,names=['市町名','名称','住所','所有者名','管理者名','野外活動スペース','Y活動面積','証明の有無','屋内活動スペース','O活動面積','駐車場面積','自家発電設備','貯水槽','無線通信設備','トイレの許容量等','宿泊施設','ヘリコプター離着陸場','食料飲料','医薬品','寝具その他生活必需品','自家発電機用燃料','その他併設施設','避難所','地域防災計画での位置づけ','備考',],skiprows=4,usecols = "B:Z")
#X=X.replace('\n', '', regex=True)
X=X.fillna('なし')
X=X.assign(緯度=0,経度=0)
for index, r in X.iterrows(): 
    
    Address = r.住所
    makeUrl = "https://msearch.gsi.go.jp/address-search/AddressSearch?q="
    s_quote = urllib.parse.quote(Address)
    response = response = requests.get(makeUrl + s_quote)

    X.loc[index,'緯度']=response.json()[0]["geometry"]["coordinates"][1]
    X.loc[index,'経度']=response.json()[0]["geometry"]["coordinates"][0]
print(X.緯度,X.経度)
X.to_csv('災害csv/物資集積所一覧.csv')

