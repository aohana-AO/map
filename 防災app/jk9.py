#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
import urllib
import requests

#物資集積所
X = pd.read_excel('youshiki3-hinanjyo.xlsx',header=None,names=['名称','住所','管理者電話','指定緊急避難場所との重複','福祉避難所','想定収容人数',],skiprows=4,usecols = "B:G")
X=X.replace('\n', '', regex=True)
X=X.fillna('なし')
X=X.assign(緯度=0,経度=0)
for index, r in X.iterrows(): 
    
    Address = r.住所
    makeUrl = "https://msearch.gsi.go.jp/address-search/AddressSearch?q="
    s_quote = urllib.parse.quote(Address)
    response = response = requests.get(makeUrl + s_quote)
    print('-------------------------------')
    print('ここまではおけ')
    print(index)
    print(r.名称)
    X.loc[index,'緯度']=response.json()[0]["geometry"]["coordinates"][1]
    X.loc[index,'経度']=response.json()[0]["geometry"]["coordinates"][0]
    print(r.住所)
    print(X.loc[index,'緯度'])
    print(X.loc[index,'経度'])
    
X.to_csv('災害csv/指定避難所一覧.csv')
print(X.緯度,X.経度)

