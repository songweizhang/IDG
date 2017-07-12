# -*- coding: utf-8 -*-

'''
    判断101-200之间有多少个素数，并输出所有素数。
'''

import math

def isPrime(n):
    if n < 2:
        print '输入错误'

    l = []
    # [2, 根号n]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True

def main():
    print isPrime(61)

if __name__ == '__main__':
    main()