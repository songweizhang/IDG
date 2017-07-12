# -*- coding: utf-8 -*-

'''
    将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
'''
import math

def isPrime(n):
    if n < 2:
        print "n error, please input num(>=2)"

    for k in range(1, int(math.sqrt(n))+1):
        if n%k == 0:
            return False
    return True

def main():
    n = 900
    print str(n) + " =",
    # n : [2 3 4 5 6 7 8 9 10]
    for k in range(2, n+1):
        while( n%k == 0 ):
            print str(k) + " *",
            n = n/k

if __name__ == '__main__':
    main()