#create visualization of the past 7 days earthquake activity
import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename="2022fev19_pastweek_all_earthquakes.geojson"
with open(filename, encoding='utf-8') as f:
    week_eq_data=json.load(f)

week_eq_dict=week_eq_data['features']
print(len(week_eq_dict))

mags, lats, lons, hover_texts =[],[],[],[]
for eq_dict in week_eq_dict:
    mag=eq_dict['properties']['mag']
    if mag>0: #because negative mag generate error
        mags.append(mag)
        lons.append(eq_dict['geometry']['coordinates'][0])
        lats.append(eq_dict['geometry']['coordinates'][1])
        hover_texts.append(eq_dict['properties']['title'])

data=[{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':hover_texts,
    'marker':{
        'size':[5*mag for mag in mags],
        'color': mags,
        'colorscale':'Electric',
        'reversescale':True,
        'colorbar':{'title':'Magnitude'},
           }
}]


my_layout=Layout(title='Earthquakes during the week of february 13th 2022')

fig={'data':data, 'layout':my_layout}
offline.plot(fig, filename='2022fev17_weekly_earthquakes.html')