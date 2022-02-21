#this is to create a visualization of fire data for the year 2021
import csv
from datetime import datetime
from plotly.graph_objs import Scattergeo , Layout
from plotly import offline

filename='fire_nrt_J1V-C2_252284.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    

    lats, lons, brights, dates=[],[],[],[]
    for row in reader:
        date=datetime.strptime(row[5], '%Y-%m-%d')
        lat=row[0]
        lon=row[1]
        bright=row[2]
        lats.append(lat)
        lons.append(lon)
        brights.append(bright)
        dates.append(date)

data=[{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':dates,
    'marker':{
        'size':[5*bright for bright in brights],
        'color': brights,
        'colorscale':'Reds',
        'colorbar': {'title':'Fire brightness'},

    }
}]

my_layout=Layout(title="Forestfires during the year 2021")
fig={'data':data,'layout':my_layout}
offline.plot(fig, filename='global_fires_2021.html')