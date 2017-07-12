# -*- coding: utf-8 -*-

'''
    一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
'''

def main():
    s = str(raw_input("input a string: \n"))
    print s
    s1 = s[::-1]
    print s1
    if s1 == s:
        print "ok"
    else:
        print "error"


if __name__ == '__main__':
    main()