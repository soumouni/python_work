#let's analyze the weather in Algeria for the past 10 years
import csv
import matplotlib.pyplot as plt
from datetime import datetime
file_name='Data/Algeria_weather_2010-2020.csv'
with open(file_name) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    
    dates, prcps=[],[]
    for row in reader:
        if row[0]=='AG000060390':
            date=datetime.strptime(row[5], '%Y-%m-%d')
            try:
                prcp=float(row[6])
            except ValueError:
                print("pb with data for", {date})
            else:
                dates.append(date)
                prcps.append(prcp)
    
    plt.style.use('seaborn')
    fig,ax=plt.subplots()
    ax.plot(dates, prcps, c='green')
    fig.autofmt_xdate()
    ax.set_title("precipations in algerie 2010", fontsize=24)
    ax.set_xlabel("dates", fontsize=14)
    ax.set_ylabel("precipations", fontsize=14)

    plt.show()