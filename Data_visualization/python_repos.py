# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/8 17:41'
__author__ = 'lee7goal'
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
import time

t1 = time.time()
# 执行API调用并存储响应
URL = 'https://api.github.com/search/repositories?q=language:python&sort=star'
r = requests.get(URL)
print("Status code:", r.status_code)
# 将api响应存储在一个变量中
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
names, stars = [], []
# print("Repositories returned:", len(repo_dicts))
# print("\nSelected information about first repository")
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    # print('Name:', repo_dict['name'])
    # print('Owner:', repo_dict['owner']['login'])
    # print('Stars:', repo_dict['stargazers_count'])
    # print('Repository:', repo_dict['html_url'])
    # print('Created:', repo_dict['created_at'])
    # print('Update:', repo_dict['updated_at'])
    # print('Description: %s \r\n\n' % repo_dict['description'])

# visualization
my_style = LS('#333366', base_style=LCS)
# visualization settings
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', stars)
# save the data visualization
print("Saving the svg......")
chart.render_to_file('python_repos.svg')
t2 = time.time()
print("Its have been Saved cost %.2f s" % (t2 - t1))
