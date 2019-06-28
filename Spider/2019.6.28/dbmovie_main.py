# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/6/28 20:10'
__author__ = 'lee7goal'
from os import path
import chnSegment
import plotWordcloud
import doubanMV_CM

if __name__ == '__main__':
    # 读取文件
    d = path.dirname(__file__)
    # 爬取一页评论
    print("爬取影评中......")
    for i in range(0,11):
        doubanMV_CM.getonepage(i)
        print('%d 页影评获得成功......' % (i+1))
    print("爬取影评完毕......")
    print("分析影评并生成词云中......")
    #  text = open(path.join(d, 'doc//十九大报告全文.txt')).read()
    text = open('.//doc/qianxun.txt', encoding='utf-8').read()

    # 若是中文文本，则先进行分词操作
    text = chnSegment.word_segment(text)

    # 生成词云
    plotWordcloud.generate_wordcloud(text)
    print("生成完毕......")