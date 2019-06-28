# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/6/28 20:13'
__author__ = 'lee7goal'
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

def generate_wordcloud(text):
    """
    输入文本生成词云，进行分词
    :param text:
    :return:
    """
    # 设置显示方式
    d = path.dirname(__file__)
    qianxun_mask = np.array(Image.open('.//Image/qx.png'))
    font_path = './/font/msyh.ttf'
    stopwords = set(STOPWORDS)
    wc = WordCloud(background_color="white",
                   max_words=2000,
                   mask=qianxun_mask,
                   stopwords=stopwords,
                   font_path=font_path
    )
    # 生成词云
    wc.generate(text)

    # 保存到本地
    wc.to_file('.//Image/千寻.png')

    # 显示图像
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()
