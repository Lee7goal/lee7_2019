# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/6/28 20:11'
__author__ = 'lee7goal'
import jieba
from os import path
from collections import Counter

def word_segment(text):
    # 计算每个词出现的频率并计入txt文件
    jieba.load_userdict(path.join('.//userdict/userdict.txt')) # 导入用户自定义词典
    jieba_word = jieba.cut(text, cut_all=False)
    data = []
    for word in jieba_word:
        data.append(word)
    dataDict = Counter(data)
    with open('.//doc/词频统计.txt', 'w', encoding='utf-8') as fw:
        for k, v in dataDict.items():
            fw.write("%s, %d\n" % (k,v))

    # 返回分词结果
    jieba_word = jieba.cut(text, cut_all=False)
    seg_list = ' '.join(jieba_word)
    return seg_list
