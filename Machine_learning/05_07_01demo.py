# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/7 12:22'
__author__ = 'lee7goal'
from collections import defaultdict
words = ['apple', 'bat', 'bar', 'atom', 'book']

by_letter = defaultdict(list)

for word in words:
    letter = word[0]
    # if letter not in by_letter:
    #     by_letter[letter] = [word]
    # else:
    #     by_letter[letter].append(word)
    by_letter[word[0]].append(word)

print(by_letter)