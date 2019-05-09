# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/9 10:01'
__author__ = 'lee7goal'
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
import json


my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'User Info'
chart.x_labels = ['London', 'England', 'Liverpool', 'Belfast', 'New Zealand', 'Canada']
chart.force_uri_protocol = 'http'

# import data of json
file_name = 'user_info.json'
with open(file_name) as f:
    info_json = json.load(f)

# analyze data
names_info = []
ages_info = []
place_info = []
place = ['London', 'England', 'Liverpool', 'Belfast', 'New Zealand', 'Canada']
place_dicts = []

for dicts in info_json:
    names_info.append(dicts['name'])
    ages_info.append(dicts['age'])
    place_info.append(dicts['location_place'])

for i in range(len(place)):
    place_dict = {
        'value': place_info.count(place[i]), 'label': place[i]
    }
    place_dicts.append(place_dict)

# analyze age
age_1, age_2, age_3, age_4, age_5, age_6 = 0, 0, 0, 0, 0, 0
"""
ages = [0-10,11-20, 21-30, 31-40, 41-50, 51-60]
for to get age in ages ,if age > 0 and age < 10: than 0-10 += 1
"""
for age in ages_info:
    if 0 < age <= 10:
        age_1 += 1
    elif 10 < age <= 20:
        age_2 += 1
    elif 20 < age <= 30:
        age_3 += 1
    elif 30 < age <= 40:
        age_4 += 1
    elif 40 < age <= 50:
        age_5 += 1
    else:
        age_6 += 1

age_dicts = [
    {'value': age_1, 'label': "0~10"},
    {'value': age_2, 'label': "10~20"},
    {'value': age_3, 'label': "20~30"},
    {'value': age_4, 'label': "30~40"},
    {'value': age_5, 'label': "40~50"},
    {'value': age_6, 'label': "50~60"}
]
# data visualization
chart.add('', place_dicts)
chart.add('', age_dicts)
chart.render_to_file('User_info_visualization.svg')
