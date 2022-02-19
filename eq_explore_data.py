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
    mags.append(eq_dicts['properties']['mag'])
    lats.append(eq_dicts['geometry']['coordinates'][1])
    lons.append(eq_dicts['geometry']['coordinates'][0])
    hover_texts.append(eq_dicts['properties']['title'])

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

    
