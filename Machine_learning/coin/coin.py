# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/17 11:23'
__author__ = 'lee7goal'
import math


def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    """find approximate inverse using binary search"""
    # 如果非标准型，先调整单位使之服从标准型
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)


def normal_approximation_to_binomial(n, p):
    """find mu and sigma corresponding to a binomial(n,p)"""
    mu = n * p
    sigma = math.sqrt(p*(1-p)*n)  # sqrt返回的是平方根
    return mu, sigma


def normal_cdf(x, mu=0, sigma=1):
     return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


# 正太cdf是一个变量在一个阈值以下的概率
normal_probability_below = normal_cdf


# 如果他不在阈值以下就在以上
def normal_probability_above(lo, mu=0, sigma=1):
    return 1-normal_cdf(lo, mu, sigma)


# 如果他小于于hi但不比lo小，那么它在区间之内
def normal_probability_between(lo, hi, mu=0, sigma=1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)


# 如果不在区间之内，那么就在区间之外
def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)


def normal_upper_bound(probability, mu=0, sigma=1):
    """returns the z for which P(Z <= z) = probability"""
    return inverse_normal_cdf(probability, mu, sigma)


def normal_lower_bound(probability, mu=0, sigma=1):
    """returns the z for which P(Z >= z) = probability"""
    return inverse_normal_cdf(1 - probability, mu, sigma)


def normal_two_sided_bounds(probability, mu=0,
                            sigma=1):
    """returns the symmetric (about the mean) bounds
    that contain the specified probability"""

    tail_probability = (1 - probability) / 2

    # 上界应有在它之上的tail_probability
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)

    # 下界应有在它之下的tail_probability
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)

    return lower_bound, upper_bound


mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)

# normal_two_sided_bounds(0.95, mu_0, sigma_0)   # (469, 531)
a = normal_upper_bound(0.95, mu_0, 15)
print(a)