import json
from plotly.graph_objs import scattergeo, layout
from plotly import offline

#explore the structure of the data
filename="Data/eq_data_1_day_m1.json"
with open(filename)as f:
    all_eq_data=json.load(f)

all_eq_dicts=all_eq_data['features']
print(len(all_eq_dicts))

mags=[]
lats, lons=[],[]
for eq_dicts in all_eq_dicts:
    mag=eq_dicts['properties']['mag']
    lon=eq_dicts['geometry']['coordinates'][0]
    lat=eq_dicts['geometry']['coordinates'][1]
    mags.append(mag)
    lats.append(lat)
    lons.append(lon)

data=[scattergeo(lon=lons, lat=lats)]
my_layout=layout(title='Global earthquakes')

fig={'data':data, 'layout':my_layout}
offline.plot(fig, filename='global_earthquakes.html')

    
