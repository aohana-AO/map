import folium
from folium.features import CustomIcon

#ベースとなる地図を作成
map = folium.Map([35.658034, 139.701636], tiles="Stamen Terrain", zoom_start=16)

#アイコンを指定
icon = CustomIcon(
   icon_image = 'img/aed.jpg'
   ,icon_size = (55, 65)
   ,icon_anchor = (30, 30)
   ,popup_anchor = (3, 3)
)

#マーカーをプロット
folium.Marker(
   location = [35.65931329218629, 139.7037205398187] #渋谷ヒカリエ
   ,icon = icon
).add_to(map)

#地図を保存
map_file = "map_itadori.html"
map.save(map_file)