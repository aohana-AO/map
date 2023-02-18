import requests
url='https://www.j-shis.bosai.go.jp/map/api/pshm/Y2021/AVR/TTL_MTTL/meshinfo.geojson?position=132.79654696,33.84750047&epsg=4326&'
result = requests.get(url).json()
print(result.keys())
print(result['features'][0]['properties'])
print(result['features'][0])
print('30年間で震度5弱以上の地震が発生する確率: '+str(float(result['features'][0]['properties']['T30_I45_PS'])*100)+'%')
print(result['features'][0]['properties']['T30_I50_PS'])
print(result['features'][0]['properties']['T30_I55_PS'])
print(result['features'][0]['properties']['T30_I60_PS'])


url='https://www.j-shis.bosai.go.jp/map/api/fltsearch?position=132.79654696,33.84750047&epsg=4326&mode=C&version=Y2019&case=MAX&period=P_T30&format=json'
result = requests.get(url).json()
print(result.keys())
print(result['Fault'][0])


'''
url='https://www.j-shis.bosai.go.jp/map/api/fltsearch?position=132.79654696,33.84750047&epsg=4326&mode=S&version=Y2019&case=MAX&period=P_T30&format=json'
result = requests.get(url).json()
print(result.keys())
print(result)
'''