# -*- coding: utf-8 -*-

import os
import time
import thread
import sys

'''
    # 主要是文件操作
    # 涉及到一些函数

'''


def fileTest():
    testdir = os.getcwd() + '/' + 'testdir'
    testfile = 'receivers.txt'
    testfile_bak = 'receivers_bak.txt'

    if not os.path.isdir(testdir):
        print '>>>>>>>>>>' + testdir + '目录不存在, 创建目录'
        os.mkdir(testdir)
        #os.__exit()

    os.chdir(testdir)

    if not os.path.isfile(testfile):
        print '>>>>>>>>>>' + testfile + '文件不存在'
        os._exit(0)
    else:
        print '>>>>>>>>>>' + testfile + '文件存在'

    #func: 读取一个文件内容
    f = open(testfile, 'r')
    content = ''
    while True:
        line = f.readline()
        if line:
            content = content + '\n' + line.strip()
        else:
            break
    #刷新缓冲区里任何还没写入的信息, 并关闭该文件, 这之后便不能再进行写入
    f.close()

    '''
        content是一个string
        lstrip(): 去掉左边的空行
    '''
    content = content.lstrip()

    #func: 写到新文件里面
    f2 = open(testfile_bak, 'a')
    f2.write(content)
    f2.close()


# 对于文件mode的理解
def fileModeTest():
    os.chdir('testdir')
    filename = 'file.txt'
    f = open(filename, 'a+')
    f.write('helloworld' + '\n')
    while True:
        line = f.readline()
        if line:
            print line
        else:
            break
    count = f.readlines()
    print count

    fo = open('file.txt', 'rw+')
    print '文件名: ' + fo.name

    line = fo.readlines()
    print '读取的数据为: %s' % (line)

    line = fo.readlines(1)
    print '读取的数据为: %s' % (line)

    line = fo.readlines(2)
    print '读取的数据为: %s' % (line)
    f.close()

def main():
    print 'test main()'
    #fileTest()

    fileModeTest()

if __name__ == '__main__':
    main()