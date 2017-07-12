# -*- coding: utf-8 -*-

'''
    一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？
'''
import math

def main():
    for i in range(10000):
        # i是from 1-9999, x是i+100的平方根, y是i+268的平方根
        x = int(math.sqrt(i + 100))
        y = int(math.sqrt(i + 268))
        # 算法思路:
        if (x * x == i + 100) and (y * y == i + 268):
            print i

if __name__ == '__main__':
    main()