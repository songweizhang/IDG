# -*- coding: utf-8 -*-

'''
    画图，学用circle画圆形。
'''
#import Tkinter
# 或者通过这样的方式:
from Tkinter import *

def center_window(root, width, heighth):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, heighth, (screenwidth - width) / 2, (screenheight - heighth) / 2)
    root.geometry(size)


def addItems(root):
    l = ['c', 'python', 'c++', 'java']
    m = ['css', 'jQuery']

    lista = Listbox(root)
    listb = Listbox(root)
    for k in l:
        lista.insert(0, k)

    for k in m:
        listb.insert(0, k)

    lista.pack()
    listb.pack()

def main():
    root = Tk()
    root.title("我的第一个窗口")
    center_window(root, 800, 600)

    addItems(root)

    root.mainloop()

if __name__ == '__main__':
    main()