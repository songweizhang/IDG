# -*- coding: utf-8 -*-

'''
    给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
'''

def func(n):
    n5 = n/10000    # 万(1)
    n4 = (n-n5*10000)/1000
    n3 = (n-n5*10000-n4*1000)/100
    n2 = (n-n5*10000-n4*1000-n3*100)/10
    n1 = n%10    # 个
    print n1, n2, n3, n4, n5

def main():
    x = int(raw_input("please input: \n"))
    func(x)

if __name__ == '__main__':
    main()