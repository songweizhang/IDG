# -*- coding: utf-8 -*-

'''
    斐波那契数列
'''

def func(n):
    if n == 1:
        return [1]

    if n == 2:
        return [1, 1]

    # 初始化
    l = [1, 1]
    for i in range(2, n):
        l.append(l[-2] + l[-1])
    print l

def main():
    func(10)

if __name__ == '__main__':
    main()