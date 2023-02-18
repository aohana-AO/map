import requests
import urllib
import pandas as pd
#広域防災拠点csv
'''
X = pd.read_excel('01youryou-shiryou1.xlsx',header=None,names=[],skiprows=5,skipfooter=8,usecols = "C:AH")
X=X.replace('\n', '', regex=True)
print(X.fillna('なし'))
X.to_csv('災害csv/広域防災拠点一覧.csv')
'''


X = pd.read_excel('01youryou-shiryou1.xlsx',header=None,names=['進出活動','物資','名称','住所','所有者名','担当課','所有者電話','所有者FAX','管理者名','管理者電話','管理者FAX','野外活動スペース','Y活動面積','証明の有無','屋内活動スペース','O活動面積','緯度','経度','UTMポイント','駐車場面積','自家発電設備','貯水槽','無線通信設備','トイレの許容量等','宿泊施設','ヘリコプター離着陸場','食料飲料','医薬品','寝具その他生活必需品','自家発電機用燃料','その他併設施設','備考',],skiprows=5,skipfooter=8,usecols = "C:AH")
X=X.replace('\n', '', regex=True)
X=X.fillna('なし')
X.to_csv('災害csv/広域防災拠点一覧2.csv')






#国土地理院API

Address = "愛媛県宇和島市吉田町立間尻 甲495−7"
makeUrl = "https://msearch.gsi.go.jp/address-search/AddressSearch?q="
s_quote = urllib.parse.quote(Address)
response = response = requests.get(makeUrl + s_quote)
print(response.json()[0]["geometry"]["coordinates"])