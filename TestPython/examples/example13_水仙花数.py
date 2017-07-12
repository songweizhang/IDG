# -*- coding: utf-8 -*-

'''
    打印出所有的"水仙花数"
    所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方
'''
import math
def main():
    for k in range(100, 1000):
        # 百位数(499)
        i = k/100
        # 百位数
        j = k/10 % 10
        # 个位数
        m = k%10
        if math.pow(i, 3) + math.pow(j, 3) + math.pow(m, 3) == k:
            print k

if __name__ == '__main__':
    main()