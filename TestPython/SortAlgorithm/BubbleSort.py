# -*- coding: utf-8 -*-

import math
#import MySQLdb
'''
    #冒泡排序
    1.冒泡排序是稳定的
    2.稳定度: 稳定
    3.空间复杂度: O(1)
    4.时间复杂度: O(n平方)
'''

list = [5, 4, 3, 2, 1]
def sort():
    for i in range(len(list)):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    print list

def sort1():
    #for i in range(len())
    pass

def main():
    print 'test main()'
    #sort()
    print math.pow(2, 32)
    print 1.09951162778e+12 - 18446744073709551615

if __name__ == '__main__':
    main()