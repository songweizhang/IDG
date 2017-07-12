# -*- coding: utf-8 -*-

'''
    输出 9*9 乘法口诀表
'''
def main():
    for i in range(1, 10):
        # 这个print表示每隔一个i,就换一次行
        print
        '''
            i=1, j: [1:1)
            i=2, j: [1:2)
            i=3, j: [1:3)
        '''
        for j in range(1, i+1):
            # 格式化输出, 为什么会有个逗号? for 循环中输出,不换行, 否则将会一行一行的输出, 很丑
            print "%d*%d=%d" % (i, j, i*j),

if __name__ == '__main__':
    main()