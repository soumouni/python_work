#try it yourself page 346
#16-1 Sitka rainfall
import csv
import matplotlib.pyplot as plt
from datetime import datetime

file_name='Data/sitka_weather_2018_simple.csv'
with open(file_name) as f:
    reader=csv.reader(f)
    header_row=next(reader)
  
    
    dates,prcps=[],[]
    for row in reader:
        prcp=float(row[3])
        date=datetime.strptime(row[2],'%Y-%m-%d')
        prcps.append(prcp)
        dates.append(date)

    fig,ax=plt.subplots()
    ax.plot(dates, prcps,c='red',alpha=0.5)
    ax.set_title('Sitka rainfall - 2018', fontsize=24)
    ax.set_xlabel('Dates', fontsize=14)
    ax.set_ylabel('Precipitations', fontsize=14)

plt.show()
   

