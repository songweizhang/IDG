# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import sys
from selenium.webdriver.common.action_chains import ActionChains

sys.path.append("..")
from CommonFunc import CommonFuncs


'''
    User: chenwei
    Date: 20170525
    Func: auto_test_Prada
'''

webAddress = 'http://idg-preprod.tunnel.nibaguai.com/prana/index.html?appkey=sipvocys9monrkvh21ela46jw05mcbkx&channels=0&disable_wx=1#/index/0'

mainAccount = '18168424783'
adminAccount = '13236590650'
teacherAccount = '13986307406'
code = '8888'

addCourseCount = 0

'''
# 馆主、管理员、老师
def switch_identiy():
    pass
'''


# 馆主登陆
def main_login():
    time.sleep(1)
    driver.find_element_by_css_selector('#content > div > div:nth-child(6) > div > div.weui-cells > button').click()

    time.sleep(1)
    driver.find_element_by_css_selector('#content > div > div.form_data > div.form_number > input[type="number"]').clear()
    driver.find_element_by_css_selector('#content > div > div.form_data > div.form_number > input[type="number"]').send_keys(mainAccount)

    time.sleep(1)
    driver.find_element_by_css_selector('#content > div > div.form_data > div.form_captcha > input[type="number"]').clear()
    driver.find_element_by_css_selector('#content > div > div.form_data > div.form_captcha > input[type="number"]').send_keys(code)

    time.sleep(1)
    driver.find_element_by_css_selector('#content > div > button').click()


# 管理员登陆
def admin_login():
    pass


# 老师
def teacher_login():
    pass


# 登陆成功后, 个人中心
def add_teacher():
    # 登陆->个人中心
    time.sleep(1)
    driver.find_element_by_css_selector('#content > div > div:nth-child(5) > button:nth-child(2)').click()

    # 登陆->个人中心->员工管理
    time.sleep(1)
    driver.find_element_by_css_selector('#content > div > ul > li:nth-child(2) > div > div.cell__left > div.choose-cell__text').click()


# 登陆成功后, 个人中心->员工管理->添加员工
def add_staff():
    # 登陆->个人中心
    time.sleep(2)
    driver.find_element_by_css_selector('#content > div > div:nth-child(5) > button:nth-child(2)').click()

    # 登陆->个人中心->员工管理
    time.sleep(2)
    driver.find_element_by_css_selector('#content > div > ul > li:nth-child(2) > div > div.cell__left > div.choose-cell__text').click()

    # 登陆->个人中心->员工管理->添加员工
    time.sleep(2)
    print '>>>>>>>>>>1 添加员工按钮'
    driver.find_element_by_css_selector('#content > div > div').click()

    # 登陆->个人中心->员工管理->添加员工->头像
    time.sleep(2)
    print '>>>>>>>>>>2 修改头像'
    driver.find_element_by_css_selector('#content > div > div.cell.avatar-cell > div.cell__right > div > div > img').click()

    # 只有微信才能改头像, 所以有个弹框
    alert_accept()

    # 登陆->个人中心->员工管理->添加员工->用户名
    time.sleep(1)
    print '>>>>>>>>>>3 添加员工 用户名'
    driver.find_element_by_css_selector('#content > div > div:nth-child(3) > div.cell__right > input').clear()
    driver.find_element_by_css_selector('#content > div > div:nth-child(3) > div.cell__right > input').send_keys('staff_chenwei')

    phone_num = int(commonfunc.read_file('MainPhoneNum.txt')) + 1
    commonfunc.write_file('MainPhoneNum.txt', str(phone_num))

    # 登陆->个人中心->员工管理->添加员工->手机号
    time.sleep(1)
    print '>>>>>>>>>>4 添加员工 手机号'
    driver.find_element_by_css_selector('#content > div > div:nth-child(5) > div.cell__right > input').clear()
    driver.find_element_by_css_selector('#content > div > div:nth-child(5) > div.cell__right > input').send_keys(str(phone_num))

    # 登陆->个人中心->员工管理->添加员工->权限
    print '>>>>>>>>>>5 添加员工 权限'
    time.sleep(1)
    driver.find_element_by_css_selector('#content > div > div.cell.select-cell > div.cell__right > select').find_element_by_xpath("//option[@value='4']").click()

    # 登陆->个人中心->员工管理->添加员工
    time.sleep(1)
    print '>>>>>>>>>>6 添加员工 添加'
    driver.find_element_by_css_selector('#content > div > div.full-btn').click()

    # print '>>>>>>>>>>修改之前'
    # 登陆->个人中心->员工管理->修改按钮
    # print '>>>>>>>>>>7 修改'
    # time.sleep(4)
    # driver.find_element_by_css_selector('#content > div > ul > li > div > div.cell__right > div > div.btn.edit').click()
    # print '>>>>>>>>>>修改之后'

    # # 登陆->个人中心->员工管理->修改按钮->用户名修改
    # time.sleep(1)
    # driver.find_element_by_css_selector('#content > div > div:nth-child(3) > div.cell__right > input').clear()
    # driver.find_element_by_css_selector('#content > div > div:nth-child(3) > div.cell__right > input').send_keys('chenwei')
    #
    # # 登陆->个人中心->员工管理->修改按钮->手机号修改
    # time.sleep(1)
    # driver.find_element_by_css_selector('#content > div > div:nth-child(5) > div.cell__right > input').clear()
    # driver.find_element_by_css_selector('#content > div > div:nth-child(5) > div.cell__right > input').send_keys('18168424783')
    #
    # # 登陆->个人中心->员工管理->修改按钮->修改
    # time.sleep(1)
    # driver.find_element_by_css_selector('#content > div > div.full-btn').click()
    #
    # # 登陆->个人中心->员工管理->删除         #content > div > ul > li:nth-child(3) > div > div.cell__right > div > div.btn.edit
    # time.sleep(3)
    # driver.find_element_by_css_selector('#content > div > ul > li:nth-child(3) > div > div.cell__right > div > div.btn.delete').click()
    #driver.find_element_by_css_selector('#app').click()
    #driver.find_element_by_css_selector('#content .teachers .cell edit-people-cell .edit-btns .btn delete').click()

    #alert_accept()

    # 返回到上一级
    driver.back()

    # 测一下卡项管理
    #card_manage()


# 卡项管理
def card_manage():
    # 登陆->个人中心
    time.sleep(2)
    driver.find_element_by_css_selector('#content > div > div:nth-child(5) > button:nth-child(2)').click()

    # 个人中心->卡项管理
    time.sleep(2)
    driver.find_element_by_css_selector('#content > div > ul > li:nth-child(1) > div').click()

    # 个人中心->卡项管理->添加会员卡
    time.sleep(2)
    driver.find_element_by_css_selector('#content > div > div').click()

    # 这边换了一个界面

    # 请设置名称->卡名称
    time.sleep(1)
    driver.find_element_by_css_selector('#content > div > div:nth-child(2) > div.cell__right > input').clear()
    driver.find_element_by_css_selector('#content > div > div:nth-child(2) > div.cell__right > input').send_keys('ttt')

    # 请设置名称->卡类型
    time.sleep(1)
    driver.find_element_by_css_selector('#content > div > div.cell.select-cell > div.cell__right > select').\
        find_element_by_xpath("//option[@value='4']").click()

    # 请设置名称->初始金额
    time.sleep(1)
    driver.find_element_by_css_selector('#content > div > div:nth-child(4) > div.cell__right > input').clear()
    driver.find_element_by_css_selector('#content > div > div:nth-child(4) > div.cell__right > input').send_keys(1234)

    # 请设置名称->价格
    time.sleep(1)
    driver.find_element_by_css_selector('#content > div > div:nth-child(5) > div.cell__right > input').clear()
    driver.find_element_by_css_selector('#content > div > div:nth-child(5) > div.cell__right > input').send_keys(01)

    # 请设置名称->有效期
    time.sleep(1)
    driver.find_element_by_css_selector('#content > div > div:nth-child(6) > div.cell__right > input').clear()
    driver.find_element_by_css_selector('#content > div > div:nth-child(6) > div.cell__right > input').send_keys(01)

    # 请设置名称->折扣
    time.sleep(1)
    driver.find_element_by_css_selector('#content > div > div:nth-child(7) > div.cell__right > input').clear()
    #driver.find_element_by_css_selector('#content > div > div:nth-child(7) > div.cell__right > input').send_keys()

    # 请设置名称->添加
    time.sleep(1)
    driver.find_element_by_css_selector('#content > div > div.add-btn > div > div > div').click()

    #alert_accept()
    time.sleep(2)
    driver.find_element_by_css_selector('#app > div.vux-alert > div > div.weui-dialog > div.weui-dialog__ft > a').click()

    driver.back()
    # 新添加的..edit && delete
    time.sleep(1)
    driver.find_element_by_css_selector('#content > div > ul > li > div > img.card').click()

    time.sleep(1)
    driver.find_element_by_css_selector('#content > div > div.delete-btn > div > div > div').click()

    # 确认删除
    time.sleep(1)
    driver.find_element_by_css_selector(
        '#app > div:nth-child(4) > div > div.weui-dialog > div.weui-dialog__ft > a.weui-dialog__btn.weui-dialog__btn_primary').click()

    # 删除成功
    time.sleep(1)
    driver.find_element_by_css_selector('#app > div.vux-alert > div > div.weui-dialog > div.weui-dialog__ft > a').click()

    driver.back()


# 开卡
def open_card():
    # 登陆->个人中心
    time.sleep(2)
    driver.find_element_by_css_selector('#content > div > div:nth-child(5) > button:nth-child(2)').click()

    time.sleep(1)
    driver.find_element_by_css_selector('#content > div > ul > li:nth-child(3) > div > div.cell__left > div.choose-cell__text').click()

    phone_num = int(commonfunc.read_file('MainPhoneNum.txt')) + 1
    commonfunc.write_file('MainPhoneNum.txt', str(phone_num))

    # 开卡->手机号
    time.sleep(1)
    driver.find_element_by_css_selector('#content > div > div:nth-child(2) > div.cell__right > input').clear()
    driver.find_element_by_css_selector('#content > div > div:nth-child(2) > div.cell__right > input').send_keys(phone_num)

    # 开卡->会员姓名
    time.sleep(1)
    driver.find_element_by_css_selector('#content > div > div:nth-child(4) > div.cell__right > input').clear()
    driver.find_element_by_css_selector('#content > div > div:nth-child(4) > div.cell__right > input').send_keys('chenwei')

    # 开卡-请选择卡的类型
    #driver.find_element_by_css_selector('#content > div > div:nth-child(6)').clear()
    driver.find_element_by_css_selector('#content > div > div:nth-child(6) > div.cell__left > div.choose-cell__text').click()

    #driver.find_element_by_id('#content > div > div:nth-child(6)').find_element_by_xpath("//option[@value='formData']").click()


# 排课
def arrange_course():
    # 登陆->个人中心
    #time.sleep(2)
    #driver.find_element_by_css_selector('#content > div > div:nth-child(5) > button:nth-child(2)').click()

    # 个人中心->排课
    time.sleep(1)
    driver.find_element_by_css_selector('#content > div > ul > li:nth-child(4) > div').click()

    # 排课->排课
    time.sleep(1)
    driver.find_element_by_css_selector('#content > div > div.bottom > div > div.operate_cancel').click()

    # 可预约3人
    time.sleep(1)
    driver.find_element_by_css_selector(
        '#content > div > div > div.vux-slider > div.vux-swiper > div:nth-child(1) > div.cell.item-cell.item-select-cell > '
        'div.cell__right.item-cell__select > select').find_element_by_xpath("//option[@value='30']").click()

    # 选择老师
    time.sleep(1)
    driver.find_element_by_css_selector('#content > div > div > div.vux-slider > div.vux-swiper > div:nth-child(1) > '
                                        'div.cell.select-cell > div.cell__right > select').find_element_by_xpath("//option[@value='52']").click()

    # 选择时间
    time.sleep(1)



#课程管理
def course_manager():
    # 登陆->个人中心
    time.sleep(2)
    driver.find_element_by_css_selector('#content > div > div:nth-child(5) > button:nth-child(2)').click()

    # 个人中心->课程管理
    time.sleep(1)
    driver.find_element_by_css_selector('#content > div > ul > li:nth-child(5) > div').click()

    add_course()


# 添加课程（属于课程管理中的一个函数）
def add_course():
    # 课程管理->添加课程
    time.sleep(1)
    driver.find_element_by_css_selector('#content > div > div.bottom > div > div.operate_confirm').click()
    # 上传图片
    # time.sleep(2)
    # driver.find_element_by_css_selector('#content > div > img.tip_img').send_keys('/Users/chenwei/Desktop/mac_ip.png')

    # 课程名称
    time.sleep(1)
    driver.find_element_by_css_selector('#content > div > div:nth-child(3) > div.cell__right > input').clear()
    driver.find_element_by_css_selector('#content > div > div:nth-child(3) > div.cell__right > input').send_keys('chenwei_course_1')

    # 所属分类
    # time.sleep(1)
    # driver.find_element_by_css_selector('#content > div > div:nth-child(5) > div.cell__right > span').click()

    # 课程人数
    time.sleep(1)
    driver.find_element_by_css_selector('#content > div > div:nth-child(7) > div.cell__right > input[type="number"]').send_keys('3')

    # 课程时长

    # 课程价格
    time.sleep(1)
    driver.find_element_by_css_selector('#content > div > div:nth-child(11) > div.cell__right > input[type="number"]').send_keys('100')

    # 课程简介
    time.sleep(1)
    driver.find_element_by_css_selector('#course_describe').send_keys(u'课程简介')

    # 添加
    time.sleep(1)
    driver.find_element_by_css_selector('#content > div > div.operate_btn > div.operate_confirm').click()

    # 确定按钮
    time.sleep(1)
    driver.find_element_by_css_selector('#app > div.vux-alert > div > div.weui-dialog > div.weui-dialog__ft > a').click()

    # 测试3个
    global addCourseCount
    if addCourseCount < 1:
        addCourseCount = addCourseCount + 1
        add_course()
    else:
        del_course()
        # 然后排课
        time.sleep(2)
        driver.find_element_by_css_selector('#content > div > div.bottom > div > div.operate_cancel').click()

        time.sleep(1)
        arrange_course()


def del_course():
    time.sleep(1)
    driver.find_element_by_css_selector('#content > div > div.o-center-box > div:nth-child(2) > div > div.btn > div:nth-child(1) > span').click()

    time.sleep(1)
    driver.find_element_by_css_selector(
        '#app > div:nth-child(4) > div > div.weui-dialog > div.weui-dialog__ft > a.weui-dialog__btn.weui-dialog__btn_primary').click()


def login(tp):
    driver.delete_all_cookies()

    time.sleep(2)
    driver.find_element_by_css_selector('#content > div > div:nth-child(6) > div > div.weui-cells > button').click()

    # 根据type区分馆长、管理员、教师
    time.sleep(2)
    driver.find_element_by_css_selector('#phone').clear()
    if tp == 1:
        driver.find_element_by_css_selector('#phone').send_keys(mainAccount)
    elif tp == 2:
        driver.find_element_by_css_selector('#phone').send_keys(adminAccount)
    elif tp == 3:
        driver.find_element_by_css_selector('#phone').send_keys(teacherAccount)

    # 验证码(都是8888)
    time.sleep(2)
    driver.find_element_by_css_selector('#captcha').clear()
    driver.find_element_by_css_selector('#captcha').send_keys(code)

    # 点击“登陆”按钮
    time.sleep(2)
    driver.find_element_by_css_selector('#bind').click()

    add_staff()
    card_manage()
    #open_card()
    #arrange_course()
    #course_manager()


# 弹出框确认按钮
def alert_accept():
    time.sleep(1)
    driver.switch_to.alert.accept()


# 弹出框取消按钮
def alert_dismiss():
    time.sleep(1)
    driver.switch_to.alert.dismiss()


def open_firefox():
    global driver
    driver = webdriver.Chrome()
    #driver = webdriver.Firefox()
    driver._is_remote = False

    # 窗口最大化, 否则不能切换tab标签, 奇怪
    driver.maximize_window()
    time.sleep(1)
    driver.get(webAddress)

    login(1)


if __name__ == '__main__':
    commonfunc = CommonFuncs()
    if not commonfunc.check_file_exists('MainPhoneNum.txt', '/Users/chenwei/Documents/py_proj/TestPython/PradaAutoTest/'):
        commonfunc.write_file('MainPhoneNum.txt', '13900000000')

    start_time = commonfunc.get_current_time()
    open_firefox()
    end_time = commonfunc.get_current_time()
    print "总共执行时间: " + str(end_time - start_time) + "s"