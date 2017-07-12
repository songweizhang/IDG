# -*- coding: utf-8 -*-

import subprocess
import socket, time, thread
import paramiko

host = '106.15.201.130'
port = 29622
username = 'root'
pkey = '/Users/chenwei/Documents/privatekey'


def main():
    print 'test main()'


if __name__ == '__main__':
    ret = subprocess.call('ping -c 1 ' + host, shell=True, stderr=subprocess.STDOUT)
    if ret == 0:

        print '>>>>>>> right'

        # # ret2 = subprocess.call('ssh -tt ' + host, shell=True, stderr=subprocess.STDOUT)
        # # ret3 = subprocess.call('pwd', shell=True, stderr=subprocess.STDOUT)
        #
        # key = paramiko.RSAKey.from_private_key_file(pkey)
        # s = paramiko.SSHClient()
        # s.load_system_host_keys()
        #
        # s.connect(host, port, username, pkey=key)
        # # stdin, stdout, stderr = s.exec_command('netstat -tunl | grep ":' + str(port) + ' "')
        # stdin, stdout, stderr = s.exec_command('netstat -tunl | grep ":29622 "')
        # out_str = stdout.read()
        # print out_str
        # if out_str.find(':' + str(port) + ' ') != -1:
        #     print 'ok'
        # else:
        #     print 'not used'


        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = s.connect_ex((host, port))
            if result == 0:
                print host, u':', port, u'端口正常'
            else:
                print host, u':', port, u'端口不能登录'
        except:
            print u'端口扫描异常'


    else:
        print '>>>>>>> wrong'
        #TODO call mail

    main()