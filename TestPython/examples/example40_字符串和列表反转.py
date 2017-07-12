# -*- coding: utf-8 -*-

'''
    将一个数组逆序输出。
'''

def main():
    test_string = "1234abcd"
    test_list = [1, 2, 3, 4, 'a', 'b', 'c', 'd']

    # [::-1] 对于string和list是通用的
    print test_string[::-1]
    print test_list[::-1]

    # 反转列表还有一种方法: reversed, 但是必须要转一下(转成list, 强转, 跟int有点像)
    print list(reversed(test_list))

if __name__ == '__main__':
    main()