# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/9 10:17'
__author__ = 'lee7goal'
import random
import json

first_name = ['jacob', 'emily', 'hannah', 'joshua', 'tyler', 'ashley']
last_name = ['adams', 'anderson', 'arnold', 'baker', 'bell', 'campbell', 'hall']
names = list()
place = ['London', 'England', 'Liverpool', 'Belfast', 'New Zealand', 'Canada']

"""
user_info = {
            'name': name,
            'age': age,
            'place': place
    }
"""
user_infos = list()


for i in range(61):
    name = random.choice(first_name) + "." + random.choice(last_name)
    names.append(name)
# print(names)

for j in range(61):
    user_info = dict()
    user_info['name'] = names[j]
    user_info['age'] = random.randint(8, 60)
    user_info['location_place'] = str(random.choice(place))
    user_infos.append(user_info)

# print(user_infos)
file_name = 'user_info.json'
with open(file_name, 'w') as f:
    json.dump(user_infos, f)
