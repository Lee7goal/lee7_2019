# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/4/11 0011 22:54'
__author__ = 'Lee7'
import re
# 确认要修改的文件
file_name = "job.txt"
# 打开文件 rb+ 格式不能encode
f = open(file_name, "rb+")
# 获取需要正则的内容，上一步不能encode,在这里decode
content = str(f.read().decode('gbk'))
# 通过正则将不需要的标签内容用sub替换为了空格
ret = re.sub(r'<[^>]+>', "", content)
# 然后通过常规操作将处理后的文本写入新的文件中
with open("【爬】"+file_name, "wb+") as k:
    k.write(ret.encode("utf-8"))
    k.close()
    f.close()
# print(ret)
