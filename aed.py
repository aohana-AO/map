from cmath import nan
from contextlib import nullcontext
import pandas as pd
import folium
from folium import plugins
import numpy
datafile = "382019_aed.csv"
lat, lon =33.8314789, 132.7649427
zoom_start = 12




webfile_name = "aed.html"

m = folium.Map(location=[lat, lon], zoom_start=zoom_start,)

marker_cluster = plugins.MarkerCluster().add_to(m)

X = pd.read_csv(datafile)

#X=X.fillna(0)


for index, r in X.iterrows(): 

   

    
    folium.Marker([r.緯度, r.経度],popup='<div id="q"><strong><h3><a href="https://maps.google.co.jp/maps?q=%s"><font size="4" color="#0000FF">%s</font></a></h3></strong><hr><p>設置位置: %s</p><p>所在地住所: <a href="https://maps.google.co.jp/maps?q=%s">%s</a></p></div> '% (r.名称,r.名称,r.設置位置,r.所在地,r.所在地),icon=folium.Icon(color='red', icon='flash')).add_to(marker_cluster)


m.save(webfile_name)

#white-space: nowrap;


