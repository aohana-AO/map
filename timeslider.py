import numpy as np
import folium
from folium import plugins
import random

#完成系、timeスライダーヒートマップ真

np.random.seed(0)

# 座標[32, 131]にランダムな揺らぎを加える
initial_data = np.random.normal(size=(15, 2)) * np.array([[1,1]]) + np.array(
    [[32, 131]]
)

print(initial_data.shape)
initial_data

# 移動する座標の差を生成
move_data = np.random.normal(size=(15, 2)) * 0.01

print(move_data.shape)
move_data
# 移動データ
data = [(initial_data + move_data * i).tolist() for i in range(2)]

print(len(data))
data
print(data)

# 座標にウェイトを追加する
for time_entry in data:
    for row in time_entry:
        weight =  random.randint(0,100)/100  # default value
        row.append(weight)
        print(row)


'''
# 地図作成 1
m = folium.Map([32.0, 131.0], zoom_start=6)

hm = plugins.HeatMapWithTime(data)

hm.add_to(m)

# 座標にウェイトを追加する
weight = 1  # default value
for time_entry in data:
    for row in time_entry:
        row.append(weight)

# 地図作成 1
m = folium.Map([32.0, 131.0], zoom_start=6)

hm = plugins.HeatMapWithTime(data)

hm.add_to(m)


'''
# 地図作成 2
# 日時で表示する
from datetime import datetime, timedelta

time_index = [
    (datetime.now() + k * timedelta(1)).strftime("%Y-%m-%d") for k in range(len(data))
]

map = folium.Map([32.0, 131.0], zoom_start=6)

hm2 = plugins.HeatMapWithTime(data, index=time_index,auto_play=False,radius=40,max_opacity=1,gradient={0.1: 'blue', 0.25: 'lime', 0.5:'yellow',0.75: 'red'})

hm2.add_to(map)


# 二種類の地図作成
#m.save("heatMapWithTime.html")
map.save("heatMapWithTime2.html")
map