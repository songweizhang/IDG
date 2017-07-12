# -*- coding: utf-8 -*-
import os
import time

# 邮件模块
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class CommonFuncs:
    # 在dir_name里面, 判断file_name是否存在
    def check_file_exists(self, file_name, dir_name):
        all_dir = '/Users/chenwei/Documents/py_proj/TestPython/' #IDG_selenium用的是这个dir, 其他要看情况
        if dir_name != None:
            all_dir = dir_name

        print all_dir
        if os.path.exists(all_dir + file_name):
            return True
        else:
            return False

    # content写入file_name
    def write_file(self, file_name, content):
        txt_file = open(file_name, 'w+')
        try:
            txt_file.write(content + '\n')
        except:
            txt_file.close()

        txt_file.close()

    # 读取file_name
    def read_file(self, file_name):
        txt_file = open(file_name, 'r')

        content = ''
        while True:
            line = txt_file.readline()
            print line
            if line:
                content += line.strip()
            else:
                break
        txt_file.close()
        return content

    # 获取当前时间
    def get_current_time(self):
        return time.time()

    # 读取文件内容，调用python自带的邮件发送方法
    def call_mail(self, title, content):
        txt_file = open(os.getcwd() + '/receivers.txt', 'r')

        # receivers存放'从rndtxt中读取的联系人，这是所有的收件人，是一个字符串'
        receivers = ''

        while True:
            line = txt_file.readline()
            if line:
                receivers = receivers + ' ' + line.strip()
            else:
                break

        txt_file.close()
        # receivers_list内容同receivers，但它是一个列表
        receivers_list = receivers.split(" ")
        del receivers_list[0]

        username = 'chenwei90@corp-ci.com'
        userpwd = 'VictorPolly123@'
        smtphost = 'smtp.exmail.qq.com'
        smtpport = 465

        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = Header('chenwei90@corp-ci.com', 'utf-8')
        msg['To'] = Header(receivers, 'utf-8')

        subject = title
        msg['subject'] = Header(subject, 'utf-8')
        try:
            smtpobj = smtplib.SMTP_SSL(smtphost, smtpport)
            smtpobj.login(username, userpwd)
            # for st in receivers_list:
            smtpobj.sendmail(username, receivers_list, msg.as_string())
            smtpobj.quit()
            print u'send succ'
        except smtplib.SMTPException:
            print u'Error: send mail failed'


