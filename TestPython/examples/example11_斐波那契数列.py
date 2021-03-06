# -*- coding: utf-8 -*-

'''
    古典问题：
    有一对兔子，从出生后第3个月起每个月都生一对兔子，
    小兔子长到第三个月后每个月又生一对兔子，
    假如兔子都不死，问每个月的兔子总数为多少？

    其实就是斐波拉契数列
'''
def main():
    '''
        1. 第一对兔子, 三个月之后, 变成1+1 = 2对
        2. 小兔子到3个月之后, 又生了一对, 变成1+ '1+1+1' + 1 = 5

        3. 第一个月 1
        4. 第二个月 1
        5. 第三个月 1+1 = 2 (生了一对)
        6. 第四个月 2+1 = 3 (又生了一对)
        7. 第五个月 3+1+1 = 5 (大兔子到3个月了,生了一对, 小兔子又到3个月了,又生了一对)
        8. 第六个月 5+1+1+1 = 8
    '''

if __name__ == '__main__':
    main()