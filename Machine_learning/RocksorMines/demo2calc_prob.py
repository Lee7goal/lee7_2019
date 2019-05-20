# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/13 18:34'
__author__ = 'lee7goal'

# get data
prob = {
    "1": 0.025,
    "2": 0.025,
    "3": 0.05,
    "4": 0.05,
    "5": 0.075,
    "6": 0.075,
    "7": 0.1,
    "8": 0.1,
    "9": 0.25,
    "10": 0.25
        }


# collection list and Probability
def viu_rate(get_num):
    prob_sum = 0
    for i in range(1, 11):
        for j in range(1, 11):
            for k in range(1, 11):
                if i + j + k == get_num:
                    prob_sum += prob[str(i)] * prob[str(j)] * prob[str(k)]
    return prob_sum


demand_input = int(input("输入刷三次图要计算获得多少次：\n"))

prob_num = viu_rate(demand_input)
print("获得 %d 次的概率为 %f " % (demand_input, prob_num))


