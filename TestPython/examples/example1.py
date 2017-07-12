# -*- coding: utf-8 -*-

import random
'''
    有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''

def main():
    count = 1
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if i != j and i != k and j != k:
                    print count, i, j, k
                    count += 1

if __name__ == '__main__':
    main()
