# -*- coding: utf-8 -*-

import time
'''
    暂停一秒输出
'''
def main():
    for k in range(10):
        print k
        time.sleep(1)

if __name__ == '__main__':
    main()