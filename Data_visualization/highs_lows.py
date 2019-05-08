# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/8 12:18'
__author__ = 'lee7goal'
import csv
from datetime import datetime
from matplotlib import pyplot as plt

file_name = 'sitka_weather_2014.csv'
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    dates, highs, lows = [], [], []
    # line_num = 0
    for row in reader:
        # line_num += 1
        # if line_num == 1:
        #     continue
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)
        low = int(row[3])
        lows.append(low)
# draw pic
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# the picture settings
plt.title("Daily high&low temperatures in 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperatures', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()


