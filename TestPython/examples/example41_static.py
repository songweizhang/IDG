# -*- coding: utf-8 -*-

'''
    模仿静态变量的作用
'''

def varFunc():
    var = 0
    print 'var = %d' %var
    var += 1

def main():
    print 'test main()'
    varFunc()


if __name__ == '__main__':
    for i in range(3):
        varFunc()