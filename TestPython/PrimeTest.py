# -*- coding: utf-8 -*-

from math import sqrt
import datetime



def is_prime1(n):
    if n <= 1:
        return False

    prime_list = []

    # 2以上可能是质数, 所以从2开始
    '''
        算法思路:
            对正整数n, 如果用到2->根号n之间的所有的整数去整除, 均无法整除
            则n为质数
    '''

    for k in range(2, n):
        for num in range(2, int(sqrt(n))+1):
            if k % num == 0 and k != num:
                break
            elif k % num != num and num == int(sqrt(n)):
                prime_list.append(k)

    return prime_list


'''
    最简单的判断, 复杂度为:

'''
def is_prime2(n):
    prime_list = []
    # for k in range(2, n-1):
    #     if n % k != 0:
    #         prime_list.append(k)
    # return prime_list

    for k in range(2, int(sqrt(n))+1):
        if n % k != 0:
            prime_list.append(k)
    return prime_list

def main():
    print 'test main()'
    start_time = datetime.datetime.now()
    #prime_list1 = is_prime1(20)
    prime_list2 = is_prime2(100)
    end_time = datetime.datetime.now()
    gap_time = end_time - start_time
    #print prime_list1
    print prime_list2
    print gap_time

if __name__ == '__main__':
    main()