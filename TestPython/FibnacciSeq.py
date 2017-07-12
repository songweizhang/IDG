# -*- coding: utf-8 -*-
import datetime

def FibnacciTest(n):
    n0 = 0
    n1 = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return FibnacciTest(n-1) + FibnacciTest(n-2)


def main():
    print 'test main()'
    print datetime.datetime.now()
    print FibnacciTest(30)
    print datetime.datetime.now()

if __name__ == '__main__':
    main()