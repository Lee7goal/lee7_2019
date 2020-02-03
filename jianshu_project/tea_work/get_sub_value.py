# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/9/8 0008 16:29'
__author__ = 'Lee7'
import os
import csv

def get_sub_values():

    ssid_list = []

    for file_name in os.listdir('./sub_data'):
        path = './sub_data/' + file_name
        with open(path, 'r',encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            for ssid in csv_reader:
                if ssid[0] == '\ufeffuser_unique_id':
                    pass
                else:
                    ssid_list.append(ssid[0])

    return ssid_list