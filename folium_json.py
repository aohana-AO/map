import folium
import json


map = folium.Map(location=[35.6809591, 139.7673068])

f = open(r'xxx.json','r',encoding="utf-8")
geometry = json.load(f)  # 辞書型で取得

folium.GeoJson(geometry).add_to(map)

# htmlに保存
map.save("folium_xxx.html")