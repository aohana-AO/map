import requests
import pandas as pd
from geopy.geocoders import Nominatim

#geopy使用

def main():
  geolocator = Nominatim(user_agent="test-dayo")
  location = geolocator.geocode("日本"+"愛媛県松山市八反地甲816")
  print("Lat, long = ",location.latitude, location.longitude)
  print("full address = ", location.address)

  # 辞書として読み取る
  loc_dict = dict(location.raw)
  print("Lat, long = ", loc_dict["lat"], loc_dict["lon"])
  print("full address = ", loc_dict["display_name"])
  print("class and type = ", loc_dict["class"], loc_dict["type"])

main()

'''
url='GET https://msearch.gsi.go.jp/address-search/AddressSearch?q=愛媛県松山市生石町397'
result = requests.get(url).json()
print(result)
'''