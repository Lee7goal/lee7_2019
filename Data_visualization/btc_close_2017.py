# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/8 16:06'
__author__ = 'lee7goal'
import json
import pygal
import time
import math
from itertools import groupby

file_name = 'btc_close_2017.json'

# save the data to file
with open(file_name) as f:
    btc_data = json.load(f)

# create data list
dates = list()
months = list()
weeks = list()
weekdays = list()
close = list()

# print everyday's info
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))
    # print("{} is month {} week {} , {} , \r\nthe close price is {} RMB\r\n".format(date, month, week, weekday, close))
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = 'The Close Price Picture In 2017 (￥)'
line_chart.x_labels = dates

# set the x show days is N = ?
N = 20
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
line_chart.add('log close price', close_log)
t1 = time.time()
print("Now is printing...")
line_chart.render_to_file("The close price picture in 2017.svg")
t2 = time.time()
print("Print Successful cost %f s" % (t2 - t1))
