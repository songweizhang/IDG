# -*- coding: utf-8 -*-

import subprocess
import socket
import random
import time
import sys
import os
sys.path.append("..")
reload(sys)
sys.setdefaultencoding('utf-8')
from CommonFunc import CommonFuncs

# 参考: http://www.cnblogs.com/wangtao1993/p/6144183.html

host = '106.15.201.130'
port = 29622
username = 'root'
pkey = '/Users/chenwei/Documents/privatekey'

port_last_exception_time = time.time()


def main():
    ret = subprocess.call('ping -c 10 ' + host, shell=True, stderr=subprocess.STDOUT)
    if ret == 0:
        print '>>>>>>> right'

        #try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((host, port))
        if result == 0:
            print host, u':', port, u'端口正常'
        else:
            # 记录当前端口异常的时间, 每隔五分钟, 发一次邮件

            rndtxt = 'interface_txt/' + str(random.randint(10000000, 99999999)) + '.txt'
            print rndtxt
            txt_file = open(rndtxt, 'w+')
            try:
                txt_file.write('host: ' + host + '\n')
                txt_file.write('port: ' + str(port) + '\n')
                txt_file.write('\n'+'该端口号不能登录' + '\n')
            except:
                txt_file.close()
            finally:
                txt_file.close()

            with open(rndtxt) as f:
                content = f.read()
            commonfunc.call_mail(u'惠氏服务器_登录异常', content)
        #except:
        #    print 'exception'
    else:
        content = 'ping了 10次全都不通'
        commonfunc.call_mail(u'惠氏服务器_ping不通', content)


if __name__ == '__main__':
    commonfunc = CommonFuncs()
    main()
