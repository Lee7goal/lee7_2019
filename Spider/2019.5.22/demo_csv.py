# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/22 13:48'
__author__ = 'lee7goal'
import csv

# with open('game_data.csv', 'r', encoding='utf-8') as csvfile:
#     csv_reader = csv.reader(csvfile)
#     for row in csv_reader:
#             print(row)
game_label = ['编号', '名称', '数量', '单个价格', '介绍']
with open('game_output.csv', 'a+', encoding='gbk', newline='') as csv_label:
    w = csv.writer(csv_label)
    w.writerow(game_label)
