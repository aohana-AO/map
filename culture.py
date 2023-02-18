from cmath import nan
from contextlib import nullcontext
import pandas as pd
import folium
from folium import plugins
import numpy
datafile = "382019_cultural_property.csv"
lat, lon =33.8314789, 132.7649427
zoom_start = 12

webfile_name = "cultural_no_tatemono.html"

m = folium.Map(location=[lat, lon], zoom_start=zoom_start,)

marker_cluster = plugins.MarkerCluster().add_to(m)

X = pd.read_csv(datafile)

for index, r in X.iterrows(): 

    if r.種類=='その他':
        
        folium.Marker([r.緯度, r.経度],popup='<div id="q"><strong><h3><a href="https://maps.google.co.jp/maps?q=%s"><font size="4" color="#0000FF">%s</font></a></h3></strong><hr><p>文化財分類: %s</p><p>種類: %s</p><p>住所: <a href="https://maps.google.co.jp/maps?q=%s">%s</a></p><p>説明ページ: <a href=%s>%s</a></p></div> '% (r.名称,r.名称,r.文化財分類,r.種類,r.愛媛県松山市住所,r.愛媛県松山市住所,r.URL,r.URL),icon=folium.Icon(color='darkgreen', icon='tree-conifer')).add_to(marker_cluster)


m.save(webfile_name)

#white-space: nowrap;