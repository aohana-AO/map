from cmath import nan
from contextlib import nullcontext
import pandas as pd
import folium
from folium import plugins
import numpy
datafile = "382019_hospital (2).csv"
lat, lon =33.8314789, 132.7649427
zoom_start = 12




webfile_name = "allhospital2.html"

m = folium.Map(location=[lat, lon], zoom_start=zoom_start,)

marker_cluster = plugins.MarkerCluster().add_to(m)

X = pd.read_csv(datafile)



#X=X.fillna(0)


for index, r in X.iterrows(): 

   
    
    if numpy.isnan(r.病床数):
        yuka=numpy.nan_to_num(r.病床数)
    else:
        yuka=r.病床数
    
    folium.Marker([r.緯度, r.経度],popup='<div id="q"><strong><h3><a href="https://maps.google.co.jp/maps?q=%s"><font size="4" color="#0000FF">%s</font></a></h3></strong><hr><p>医療機関の種類: %s</p><p>診療科目: %s</p><p>病床数: %d</p><p>住所: <a href="https://maps.google.co.jp/maps?q=%s">%s%s</a></p></div> '% (r.名称,r.名称,r.医療機関の種類,r.診療科目,yuka,r.住所,r.都道府県名,r.住所),icon=folium.Icon(color='red', icon='plus-sign')).add_to(marker_cluster)


m.save(webfile_name)

#white-space: nowrap;