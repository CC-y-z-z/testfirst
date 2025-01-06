# 在模块random中
# 函数randint()以两个整数作为参数，并随机返回一个位于这两个整数之间（含）的整数
from random import randint
a=randint(2,8)
print(a)
# 函数choice()以一个列表或元组作为参数，并随机返回其中的一个元素
from random import choice
players=['charles','martina','michael','florence','eli']
first_up=choice(players)
print(first_up)