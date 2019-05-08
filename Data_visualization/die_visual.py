# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/8 9:07'
__author__ = 'lee7goal'
from die import Die
import pygal

# create a Die 6
die1 = Die()
die2 = Die(7)
die3 = Die(8)
# to roll anytimes die and save the data
results_die1 = list()
results_die2 = list()
results_die3 = list()
for roll_num1 in range(50000):
    result = die1.roll()
    results_die1.append(result)
for roll_num2 in range(50000):
    result = die2.roll()
    results_die2.append(result)
for roll_num3 in range(50000):
    result = die3.roll()
    results_die3.append(result)
# print(results)
# analyze data
frequencies1 = list()
frequencies2 = list()
frequencies3 = list()
# max_result = die1.num_sides + die2.num_sides + die3.num_sides
for value in range(1, die1.num_sides+1):
    frequency1 = results_die1.count(value)
    frequencies1.append(frequency1)
for value in range(1, die2.num_sides+1):
    frequency2 = results_die2.count(value)
    frequencies2.append(frequency2)
for value in range(1, die3.num_sides+1):
    frequency3 = results_die3.count(value)
    frequencies3.append(frequency3)
# print(frequencies)
# data visualization
hist = pygal.Bar()
hist.title = "Results of rolling D5-D6-D7 100000 times"
hist.x_labels = [str(i) for i in range(1, die3.num_sides+1)]
# print(hist.x_labels)
hist.x_title = "Results"
hist.y_title = "Frequency of Results"
hist.add('D6', frequencies1)
hist.add('D7', frequencies2)
hist.add('D8', frequencies3)
# file name
file_name = 'die_visual.svg'
hist.render_to_file(file_name)
print("%s have been saved successful" % file_name)
