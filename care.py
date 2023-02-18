import pandas as pd
import numpy as np
import folium
from folium import plugins
datafile = "302019_care_service3.csv"
lat, lon =33.8920372, 132.4286822
zoom_start = 18




webfile_name = "care2.html"

m = folium.Map(location=[lat, lon], zoom_start=zoom_start,)

marker_cluster = plugins.MarkerCluster().add_to(m)

X = pd.read_csv(datafile)

X=X.fillna(0)


for index, r in X.iterrows(): 
    p = '<div id="q"><h4>名称 : %s</h4><p>実施サービス : %s</p><hr><a href="https://www.google.co.jp/maps?q=%f,%f">マップ : %s</a><br><p>電話番号 : %s<p/><br><p>fax番号 : %s<p/><br><p>法人の名称 : %s<p/><br><p>事業所番号 : %s<p/><br></div>' % (r.介護サービス事業所名称, r.実施サービス, r.緯度, r.経度, r.住所, r.電話番号, r.FAX番号,r.法人の名称, r.事業所番号) 
    folium.Marker([r.緯度, r.経度], popup=p,icon=folium.Icon(color='red', icon='flash')).add_to(marker_cluster)


m.save(webfile_name)

#white-space: nowrap;