# -*- coding: utf-8 -*-

'''
    输入三个整数x,y,z，请把这三个数由小到大输出
'''
def main():
    l = []
    for i in range(3):
        l.append(int(raw_input('integer:\n')))

    l.sort()
    print l

if __name__ == '__main__':
    main()