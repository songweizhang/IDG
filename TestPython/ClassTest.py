# -*- coding: utf-8 -*-
aaaaaaaaaaa

class ClassTest:
    m_count = 0

    def __init__(self, name, sex):
        self.m_name = name
        self.m_sex = sex
        self.m_count += 1

    def echoCount(self):
        print '>>>>>>>>>>current count = ' + self.m_count

    def echoClass(self):
        print '>>>>>>>>>>Name : ', self.m_name, 'Sex : ', self.m_sex

    def parentTest(self):
        print '>>>>>>>>>>', 'parentTest'


class parentTest:
    count = 0

    def __init__(self):
        print '>>>>>>>>>>', '这是parent的init方法'

    def echoTest(self):
        print self.m_count


class clildTest(parentTest):
    def __init__(self):
        print '>>>>>>>>>>', '这是child的init方法'


test1 = ClassTest('chenwei', 0)
test2 = ClassTest('yunansong', 1)
test1.echoClass()
test2.echoClass()

del test1, test2

#test3 = childTest()
