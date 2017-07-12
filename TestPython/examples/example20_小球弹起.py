# -*- coding: utf-8 -*-
'''
    一球从100米高度自由落下
    每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

    求两个东西, 1是经过了多少米, 2是反弹多高
    1:  100 100+50+50  100+50+50+25+25
    2:  100 100/2=50  50/2=25  25/2=2
'''
import math

start_height = 100
rebound_rate = 0.5
meter_list = [100]

def rebound(time):
    m = start_height*(rebound_rate ** (time))
    return m

'''
    1.第一次落地, 经过了100米
    2.第二次落地, 经过了100+50+50米
    3.第三次落地, 经过了100+50+50+25+25米
'''
def get_all_meter(time):
    for k in range(1, time):
        meter = start_height + rebound(time-1)*2
        meter_list.append(meter)

def main():
    #print rebound(10)
    print get_all_meter(11)

if __name__ == '__main__':
    main()