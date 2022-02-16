import csv
import matplotlib.pyplot as plt
from datetime import datetime

file_1='Data/death_valley_2018_simple.csv'
file_2='data/sitka_weather_2018_simple.csv'

with open(file_1) as f1:
    reader=csv.reader(f1)
    header_row= next(reader)

    dates, highs, lows=[],[],[]
    for row in reader:
        date=datetime.strptime(row[2],'%Y-%m-%d')
        try:
            high=int(row[4])
            low=int(row[5])
        except ValueError:
            print('missing data for', {date})
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

with open(file_2) as f2:
    reader=csv.reader(f2)
    header_row=next(reader)

    dates2, highs2, lows2=[],[],[]
    for row in reader:
        date=datetime.strptime(row[2], '%Y-%m-%d')
        high=int(row[5])
        low=int(row[6])
        dates2.append(date)
        highs2.append(high)
        lows2.append(low)

#fig,ax=plt.subplots()
fig,ax=plt.subplots(figsize=(15,9))
ax.plot(dates, highs, c='red', alpha=0.6)
ax.plot(dates, lows, c='red', alpha=0.6)
plt.fill_between(dates, highs, lows, facecolor='red', alpha=0.1)
ax.set_title('death valley')

ax.plot(dates2, highs2, c='green', alpha=0.6)
ax.plot(dates2, lows2, c='green', alpha=0.6)
plt.fill_between(dates2, highs2, lows2, facecolor='green', alpha=0.1)
ax.set_title('Sitka')

plt.ylim(0,140)
fig.autofmt_xdate()

plt.show()

