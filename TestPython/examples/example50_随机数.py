# -*- coding: utf-8 -*-

'''
    生成随机数
'''
import random

def genRandom():
    # [0, 1)
    #print random.random()

    # [10, 20], 各种整数, 保留到小数点后面10位
    #print random.uniform(10, 20)

    # [10, 20], 只保留整数
    #print random.randint(10, 20)

    # [0, n), 返回的是整数, 如果n是1的话, 返回的是0, 注意和random.random()的区别
    #print random.randrange(10)

    # [start, end), 返回的是start-end之间的整数, 这个end必须大于start(不能等于, 不然会报错)
    #print random.randrange(2, 3)

    # [start, end, step], 返回的是start、start加上各种步长的结果
    #print random.randrange(2, 10, 3)

    # 从sequence中获取一个元素
    # 如果sequence是一个string, 返回的是随机的一个字符
    # 如果sequence是一个列表, 返回的是随机的一个元素
    # 如果....
    print random.choice("python")
    print random.choice([1,2,3,4,5])


def main():
    genRandom()

if __name__ == '__main__':
    main()