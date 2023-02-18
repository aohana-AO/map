#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
import urllib
import requests

#緊急避難
X = pd.read_excel('youshiki1-hinanbasyo (1).xlsx',header=None,names=['名称','住所','管理者電話','指定避難場所との重複','洪水','がけ崩れ土石流地すべり','高潮','地震','津波','大規模火災','内水氾濫','火山現象','想定収容人数',],skiprows=4,usecols = "B:N")
X=X.replace({'指定避難場所との重複': {1: '〇'},'洪水': {1: '〇'},'がけ崩れ土石流地すべり': {1: '〇'},'高潮': {1: '〇'},'地震': {1: '〇'},'大規模火災': {1: '〇'},'内水氾濫': {1: '〇'},'火山現象': {1: '〇'},'津波': {1: '〇'},})
X=X.fillna('なし')
X=X.assign(緯度=0,経度=0)
X=X.replace('\n', '',)
list=[]

for index, r in X.iterrows(): 
    
    Address = r.住所
    makeUrl = "https://msearch.gsi.go.jp/address-search/AddressSearch?q="
    s_quote = urllib.parse.quote(Address)
    response = response = requests.get(makeUrl + s_quote)
   
    print('-------------------------------')
    print('ここまではおけ')
    print(index)
    print(r.名称)
    
    try:
        X.loc[index,'緯度']=response.json()[0]["geometry"]["coordinates"][1]
        X.loc[index,'経度']=response.json()[0]["geometry"]["coordinates"][0]
        
        print(r.住所)
        print(X.loc[index,'緯度'])
        print(X.loc[index,'経度'])
        
    except IndexError:
        list.append(index)
        

# Error
    
    
X.to_csv('災害csv/指定緊急避難所一覧2x.csv')
print(list)
