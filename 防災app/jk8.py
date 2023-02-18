#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd

#物資集積所
'''
'''
X = pd.read_excel('02youryou-shiryou2.xlsx',header=None,names=['市町名','名称','住所','所有者名','管理者名','野外活動スペース','Y活動面積','証明の有無','屋内活動スペース','O活動面積','駐車場面積','自家発電設備','貯水槽','無線通信設備','トイレの許容量等','宿泊施設','ヘリコプター離着陸場','食料飲料','医薬品','寝具その他生活必需品','自家発電機用燃料','緯度','経度','UTMポイント','その他併設施設','避難所','地域防災計画での位置づけ','備考',],skiprows=4,usecols = "B:AC")
#X=X.replace('\n', '', regex=True)
X=X.fillna('なし')
print(X)


X.to_csv('災害csv/活動拠点候補一覧.csv')