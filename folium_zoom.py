
from contextlib import nullcontext
import pandas as pd
import folium
from folium import plugins


datafile = "xxx.csv"
lat, lon = 33.8314789, 132.7649427
zoom_start = 12

webfile_name = "xxx.html"

m = folium.Map(location=[lat, lon], zoom_start=zoom_start, )

marker_cluster = plugins.MarkerCluster().add_to(m)

X = pd.read_csv(datafile)

# X=X.fillna(0)


for index, r in X.iterrows():
    if r[6]!=0:
        folium.Marker([r[5], r[4]],
                      popup=r[6], icon=folium.Icon(color='red', icon='plus-sign')).add_to(
            marker_cluster)

m.save(webfile_name)

# white-space: nowrap;