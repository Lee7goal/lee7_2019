# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/29 13:42'
__author__ = 'lee7goal'
from PIL import Image
import pytesseract
import os
"""
# 对验证码图片进行处理
def covert_img(img, threshold):
    # 处理灰度
    img = Image.open(img)
    img = img.convert('L')
    pixels = img.load()
    for x in range(img.width):
        for y in range(img.height):
            if pixels[x, y] > threshold:
                pixels[x, y] = 255
            else:
                pixels[x, y] = 0
    img.show()
    return img

result = covert_img('demo4.png', 150)
result = pytesseract.image_to_string(result)
print(result)
"""""


def covert_img(img):
    data = img.getdata()
    w,h = img.size
    img = img.convert('L')
    count = 0
    for x in range(1,h-1):
        for y in range(1, h - 1):
            # 找出各个像素方向
            mid_pixel = data[w * y + x]
            if mid_pixel == 0:
                top_pixel = data[w * (y - 1) + x]
                left_pixel = data[w * y + (x - 1)]
                down_pixel = data[w * (y + 1) + x]
                right_pixel = data[w * y + (x + 1)]

                if top_pixel == 0:
                    count += 1
                if left_pixel == 0:
                    count += 1
                if down_pixel == 0:
                    count += 1
                if right_pixel == 0:
                    count += 1
                if count > 4:
                    img.putpixel((x, y), 0)
    img.show()
    return img

img = Image.open('demo4.png')
result = covert_img(img)
result = pytesseract.image_to_string(result)
print(result)