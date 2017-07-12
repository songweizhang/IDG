# -*- coding: utf-8 -*-

'''

'''

def exchange(a, b):
    b,a = a,b
    return a, b

def main():
    a = 50
    b = 20
    a, b = b, a
    print a, b

if __name__ == '__main__':
    main()