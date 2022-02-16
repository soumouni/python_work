import csv
import matplotlib.pyplot as plt
from datetime import datetime

#read csv file
filename='Data/death_valley_2018_simple.csv'
with open (filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)

    #get dates, highs and lows temperatures from this file
    dates, highs, lows=[],[],[]
    for row in reader:
        current_date=datetime.strptime(row[2],'%Y-%m-%d')
        try:
            high=int(row[4])
            low=int(row[5])
        except ValueError:
            print('missing data for', {current_date})
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
plt.style.use('seaborn')
fig,ax=plt.subplots()
ax.plot(dates, highs,c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='pink', alpha=0.4)

ax.set_title("low and high temperatures dor deth valley during 2018")
ax.set_xlabel("dates")
fig.autofmt_xdate()
ax.set_ylabel("temperatures (deg F)")

plt.show()