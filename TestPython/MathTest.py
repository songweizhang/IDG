# -*- coding: utf-8 -*-

import math
import random


def mathTest():
    a = 2
    print math.exp(a) #7.38905609893

    f = math.pi
    print math.modf(f)    #整数部分, 小数部分
    print math.ceil(4.1)  #5
    print math.floor(4.1) #4

    print math.pow(3, 4)
    print 3**4

    print round(4.464444, 1)
    print abs(-123)

    print random.choice(range(2))

    print '>>>>>>>>>>range>>>>>>>>>'
    print range(3)                  #返回[0, x)的整数
    print range(5, 10)              #
    print range(5, 10, 3)

    print '>>>>>>>>>>>>randrange>>>>>>>>>>>>>'
    print random.randrange(1)
    print random.randrange(5, 10)
    print random.randrange(5, 10, 3)
    #print random.random()           #[0,1), 包括小数

    list = [10, 8, 9, 14, 17]
    print list
    random.shuffle(list)
    print list
    #print random.choice(list)

    random.seed()
    print random.random()
    print random.uniform(0, 1)

def main():
    mathTest()

if __name__ == '__main__':
    main()