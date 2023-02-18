import requests
import pandas as pd
url='http://geoapi.heartrails.com/api/json?method=searchByGeoLocation&x=132.7965469&y=33.84750047'
result = requests.get(url).json()
print(result['response']['location'][1].keys())
x=0
for i in result['response']['location']:
    print('〒'+result['response']['location'][x]['postal'],end='')
    print(result['response']['location'][x]['prefecture'],end='')
    print(result['response']['location'][x]['city'],end='')
    print(result['response']['location'][x]['town'],end='')
    print(' 緯度'+result['response']['location'][x]['x'],end='')
    print(' 経度'+result['response']['location'][x]['y'])
    x+=1

url2='https://mreversegeocoder.gsi.go.jp/reverse-geocoder/LonLatToAddress?lat=33.84750047&lon=132.7965469'
result2=requests.get(url2).json()
print(result2['results']['muniCd'])
print(result2['results']['lv01Nm'])

code=result2['results']['muniCd']
mati=result2['results']['lv01Nm']

datefile='000730858 (3).xlsx'
X = pd.read_excel(datefile,engine='openpyxl',sheet_name='R1.5.1現在の団体',)

X = X.rename(columns={'都道府県名\n（漢字）': '都道府県名','市区町村名\n（漢字）': '市区町村名'})

for index, r in X.iterrows(): 
    if str(r.団体コード)[:-1]==str(code):
        ken2=r.都道府県名
        si=r.市区町村名

print(ken2+si+mati)

##url3='https://nominatim.openstreetmap.org/reverse?format=json&lat=33.84750047&lon=132.7965469&zoom=18&addressdetails=1'
##result3=requests.get(url3).json()
##print(result3)