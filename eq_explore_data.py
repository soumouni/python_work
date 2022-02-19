import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#explore the structure of the data
filename="eq_data_30_day_m1.json"
with open(filename) as f:
    all_eq_data=json.load(f)

all_eq_dicts=all_eq_data['features']
print(len(all_eq_dicts))

mags,lats, lons, hover_texts=[],[],[],[]
for eq_dicts in all_eq_dicts:
    mag=eq_dicts['properties']['mag']
    lon=eq_dicts['geometry']['coordinates'][0]
    lat=eq_dicts['geometry']['coordinates'][1]
    title=eq_dicts['properties']['title']
    mags.append(mag)
    lats.append(lat)
    lons.append(lon)
    hover_texts.append(title)

data=[{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':hover_texts,
    'marker':{
        'size':[5*mag for mag in mags],
        'color':mags,
        'colorscale':'Electric',
        'reversescale':True,
        'colorbar':{'title':'Magnitude'}
    }
}]
my_layout=Layout(title='Global earthquakes')

fig={'data':data, 'layout':my_layout}
offline.plot(fig, filename='global_earthquakes.html')

    
