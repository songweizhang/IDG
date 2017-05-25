# -*- coding: utf-8 -*-

from selenium import webdriver
import time
from CommonFunc import CommonFuncs

# 显式等待
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

'''
    User: chenwei
    Date: 20170326 -> 20170509
    Func: auto_test_IDG
'''

# "我的应用"的下面
appid = "123456"
appkey = "orhudjjat82bea3yysfowcsexhni0mpu"
appsecret = "skn9yz7uxi4xfpyh6ahbenawjvdwqjco"

all_h, cur_h = '', ''   # 窗口的标签handler
cur_service_k = 0       # 当前测的是第几个服务(admin是第一个)
service_num = 28        # 总共28个服务


# 点击登录按钮, 调用login方法
def click_login():
    driver.find_element_by_class_name("header-login-btn").click()

    time.sleep(1)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.get("http://idg-preprod.tunnel.nibaguai.com/admin/main.php?action=login.html")

    login()


# 输入账户、密码, 点击按钮, 弹出"创建应用"对话框
def login():
    print ">>>测试登陆",
    time.sleep(1)
    driver.find_element_by_name("username").send_keys("chenwei")
    time.sleep(1)
    driver.find_element_by_name("password").send_keys("chenwei")
    time.sleep(1)
    driver.find_element_by_class_name("btn-login").click()

    driver.switch_to.window(driver.window_handles[0])

    print " ...ok"
    time.sleep(1)
    # 这边应该调用create_platform(), 应为不要创建太多平台(暂时不能删除), 所以先注释掉, 直接调create_app方法

    create_platform()
    #app_operate()
    #app_service()


# 登出
def login_out():
    time.sleep(2)
    driver.find_element_by_css_selector('#wrapper > nav > div.options.options-right > ul > li:nth-child(3) > a').click()


# 创建应用平台
def create_platform():
    print ">>>测试创建应用平台",
    driver.find_element_by_id("create").click()

    time.sleep(1)
    driver.find_element_by_css_selector("#add_platform .form-control").send_keys(u"测试平台2")

    # 空格代表祖先关系
    time.sleep(1)
    driver.find_element_by_css_selector("#add_platform .modal-footer .btn-default").click()
    #driver.find_element_by_css_selector("#add_platform .modal-footer .btn-primary").click()
    print " ...ok"

    create_app()


# 创建应用
def create_app():
    print ">>>测试创建应用",
    time.sleep(2)
    driver.find_element_by_css_selector(".cards .card-new:last-child").click()

    time.sleep(2)
    driver.find_element_by_name("appname").send_keys(u"测试app1")

    time.sleep(1)
    driver.find_element_by_name("owner").send_keys(18168424788)

    time.sleep(1)
    driver.find_element_by_name("register_tpl").send_keys(u"模板test")

    time.sleep(1)
    driver.find_element_by_name("nickname_prefix").send_keys("1234567")

    time.sleep(2)
    # .代表class #代表id
    #driver.find_element_by_css_selector("#create_app .modal-footer .btn-primary").click()
    driver.find_element_by_css_selector("#create_app .modal-footer .btn-default").click()
    print " ...ok"

    app_enter_official()


# "我的应用"->进入官网
def app_enter_official():
    print ">>>测试进入官网",
    # 此时在主界面, 停顿2秒
    time.sleep(2)
    # 根据AppKey找到"进入官网"这个按钮, 点击
    driver.find_element_by_css_selector("a[href*="+appkey+"]:not(.bt)").click()

    time.sleep(4)
    # 把"官网"关闭, 回退到之前的主界面
    close_label()

    # (1)就代表开发
    driver.find_element_by_css_selector("a[href*=" + appkey + "].bt:nth-child(1)").click()
    print " ...ok"

    app_develop()
    app_operate()


# "我的应用"->"开发"
def app_develop():
    print ">>>测试开发",
    # 新建接口->Name
    time.sleep(1)
    driver.find_element_by_id("title").send_keys("interface_test")

    time.sleep(1)
    driver.find_element_by_id("curPathOp").click()

    time.sleep(1)
    '''
        1. #表示找ID
        2. >表示下面的子元素
        3. 然后获取li标签, nth-child表示li下面的第几个子元素(1开始, 而不是0), 下面只测一下get
        4. >又表示子元素
        5. li下面有一个子元素叫做a标签
    '''
    # pathOps > li:nth-child(1) > a
    driver.find_element_by_css_selector("#pathOps > li:nth-child(2) > a:nth-child(1)").click()

    time.sleep(1)
    driver.find_element_by_id("path").send_keys("path_test_get")

    time.sleep(1)
    driver.find_element_by_id("tag").send_keys("tag_test")
    time.sleep(1)
    driver.find_element_by_id("desc").send_keys("desc_test")

    # 点击add按钮
    time.sleep(1)
    driver.find_element_by_id("btn_add_param").click()

    time.sleep(1)
    driver.find_element_by_id("modal_param_name").send_keys("param_name")

    # 通过id, 获取下拉框的数值(参考: http://blog.csdn.net/liuchunming033/article/details/46802643)
    time.sleep(1)
    driver.find_element_by_id("modal_param_located_in").find_element_by_xpath("//option[@value='formData']").click()

    time.sleep(1)
    driver.find_element_by_id("modal_param_desc").send_keys("param_desc")

    time.sleep(1)
    driver.find_element_by_id("radio_required_no").click()

    time.sleep(1)
    #driver.find_element_by_id("modal_param_schema").find_element_by_xpath("//option[@value='boolean']").click()

    time.sleep(2)
    # 创建一个接口
    driver.find_element_by_css_selector("#edit_param_modal .modal-footer .btn-primary").click()

    time.sleep(2)
    # 删除接口
    driver.find_element_by_css_selector("table tr:nth-child(2) td:last-child .btn-danger").click()

    time.sleep(1)
    # dismiss是取消, accept是接受(对应于弹出框上面的 '取消' '确定')
    driver.switch_to_alert().dismiss()

    # 保存设置 && delete
    time.sleep(1)
    #driver.find_element_by_id("btn_save").click()
    driver.find_element_by_id("btn_delete").click()
    time.sleep(1)
    driver.switch_to_alert().dismiss()

    # 暂停1s, 返回主界面, 测试运营
    time.sleep(1)
    driver.back()
    print " ...ok"


# "我的应用"->"运营"
def app_operate():
    print ">>>测试运营",
    time.sleep(1)
    driver.find_element_by_css_selector("a[href*="+appkey+"].bt:nth-child(2)").click()
    print " ...ok"

    # "运营" 界面, 添加一个channel、"正常渠道"、"已经用渠道"、"基础配置"、"禁用", 最后是 "返回"按钮的测试
    time.sleep(1)
    add_channel()


# "我的应用"->"运营"->"正常渠道"->"正常渠道"(有两个标签, 正常渠道+已禁用渠道)
def add_channel():
    print ">>>测试'新增渠道'",
    time.sleep(1)
    '''
        1. [], 中括号, 里面跟的是属性, 如href、data-target
        2. =是key value的写法, h1[title], h1[title="Logo"]
        3. 所以那个''是必须的
    '''
    driver.find_element_by_css_selector("[data-target='#add_channel']").click()

    time.sleep(1)
    driver.find_element_by_css_selector('#add_channel .modal-dialog .modal-content .modal-body .form-group [name="name"]').send_keys("channel_test")

    time.sleep(1)
    driver.find_element_by_css_selector('#add_channel .modal-dialog .modal-content .modal-body .form-group [name="owner_name"]').send_keys("owner_test")

    phone_num = int(commonfunc.read_file('PhoneNum.txt')) + 1
    commonfunc.write_file('PhoneNum.txt', str(phone_num))

    time.sleep(1)
    driver.find_element_by_css_selector('#add_channel .modal-dialog .modal-content .modal-body .form-group [name="owner"]').send_keys(str(phone_num))

    # 监测手机号
    time.sleep(1)
    driver.find_element_by_id('check_phone').click()

    time.sleep(2)
    #driver.find_element_by_css_selector('#add_channel .modal-dialog .modal-content .modal-footer .btn-default').click()
    driver.find_element_by_css_selector('#add_channel .modal-dialog .modal-content .modal-footer .btn-primary').click()

    time.sleep(1)
    print " ...ok"

    delete_channel()


# "我的应用"->"运营"->"禁用"
def delete_channel():
    print ">>>测试'删除渠道'",
    time.sleep(1)
    driver.find_element_by_css_selector("#channel_table > tbody > tr > td:nth-child(5) > a.btn.btn-danger.btn-xs").click()
    time.sleep(1)
    driver.find_element_by_css_selector("#block_channel .modal-dialog .modal-content .modal-body .form-group .form-control").send_keys("just a test")

    time.sleep(1)
    driver.find_element_by_css_selector('#block_channel .modal-dialog .modal-content .modal-footer .btn-primary').click()

    print " ...ok"
    # 禁用之后, 到"已禁用渠道"里面去查看

    already_deleted_channel()


# "我的应用"->"运营"->"已禁用渠道"
def already_deleted_channel():
    print ">>>测试'已禁用渠道'",
    time.sleep(1)
    driver.find_element_by_css_selector('ul.nav:nth-child(1) > li:nth-child(2) > a:nth-child(1)').click()
    print " ...ok"

    basic_config()


# "我的应用"->"运营"->"基础配置"
def basic_config():
    print ">>>测试'基础配置'",
    time.sleep(1)
    driver.find_element_by_css_selector("[data-target='#edit_config']").click()

    time.sleep(2)
    driver.find_element_by_id("no_apply").click()

    time.sleep(2)
    # driver.find_element_by_css_selector('#edit_config .modal-dialog .modal-content .modal-footer .btn-default').click()
    driver.find_element_by_css_selector("#edit_config .modal-dialog .modal-content .modal-footer .btn-primary").click()

    time.sleep(2)
    driver.find_element_by_css_selector('a[href="main.php?action=index.html"].btn-default').click()

    time.sleep(1)
    print " ...ok"

    app_service()


# "我的应用"->"服务", 这边到了所有的服务列表, 之后所有的服务测试, 均从这个界面开始
def app_service():
    # 开始测试所有服务
    # "服务"是第三个按钮, 所以nth-child(3)
    time.sleep(2)
    driver.find_element_by_css_selector("a[href*=" + appkey + "].bt:nth-child(3)").click()
    test_next_service()


def test_next_service():
    # 全局变量, 每次进入该函数时, +1
    global cur_service_k
    cur_service_k += 1

    # 测试"服务说明", 这是所有服务公用的
    app_service_service_explanation()
    # 停顿3秒, 关闭掉
    time.sleep(3)
    close_label()

    # 测试"api列表", 这也是所有服务公用的
    time.sleep(1)
    app_service_api_list()
    # swagger文档打开时间比较长, 所以停了8s后将其关闭
    time.sleep(5)
    close_label()

    # "服务配置"是第3个按钮
    time.sleep(2)
    driver.find_element_by_css_selector('li.card-auto:nth-child(' + str(cur_service_k) + ') > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > a:nth-child(3)').click()

    if cur_service_k == 1:
        print ">>>" + str(cur_service_k) + " 测试账号服务",
        app_service_service_config1()
        print " ...ok"
    elif cur_service_k == 2:
        print ">>>" + str(cur_service_k) + " 测试用户服务",
        app_service_service_config2()
        print " ...ok"
    elif cur_service_k == 3:
        print ">>>" + str(cur_service_k) + " 测试支付服务",
        app_service_service_config3()
        print " ...ok"
    elif cur_service_k == 4:
        print ">>>" + str(cur_service_k) + " 测试实体表格服务",
        app_service_service_config4()
        print " ...ok"
    elif cur_service_k == 5:
        print ">>>" + str(cur_service_k) + " 测试直播服务",
        app_service_service_config5()
        print " ...ok"
    elif cur_service_k == 6:
        print ">>>" + str(cur_service_k) + " 测试push服务",
        app_service_service_config6()
        print " ...ok"
    elif cur_service_k == 7:
        print ">>>" + str(cur_service_k) + " 测试活动服务",
        app_service_service_config7()
        print " ...ok"
    elif cur_service_k == 8:
        print ">>>" + str(cur_service_k) + " 测试微官网服务",
        app_service_service_config8()
        print " ...ok"
    elif cur_service_k == 9:
        print ">>>" + str(cur_service_k) + " 测试预约服务",
        app_service_service_config9()
        print " ...ok"
    elif cur_service_k == 10:
        print ">>>" + str(cur_service_k) + " 测试启动页服务",
        app_service_service_config10()
        print " ...ok"
    elif cur_service_k == 11:
        print ">>>" + str(cur_service_k) + " 测试CMS服务",
        app_service_service_config11()
        print " ...ok"
    elif cur_service_k == 12:
        print ">>>" + str(cur_service_k) + " 测试微海报服务",
        app_service_service_config12()
        print " ...ok"
    elif cur_service_k == 13:
        print ">>>" + str(cur_service_k) + " 测试代理服务",
        app_service_service_config13()
        print " ...ok"
    elif cur_service_k == 14:
        print ">>>" + str(cur_service_k) + " 测试权限管理服务",
        app_service_service_config14()
        print " ...ok"
    elif cur_service_k == 15:
        print ">>>" + str(cur_service_k) + " 测试api_tool服务",
        app_service_service_config15()
        print " ...ok"
    elif cur_service_k == 16:
        print ">>>" + str(cur_service_k) + " 测试积分商城服务",
        app_service_service_config16()
        print " ...ok"
    elif cur_service_k == 17:
        print ">>>" + str(cur_service_k) + " 测试官网服务",
        app_service_service_config17()
        print " ...ok"
    elif cur_service_k == 18:
        print ">>>" + str(cur_service_k) + " 测试商城服务",
        app_service_service_config18()
        print " ...ok"
    elif cur_service_k == 19:
        print ">>>" + str(cur_service_k) + " 测试微信公共号托管服务",
        app_service_service_config19()
        print " ...ok"
    elif cur_service_k == 20:
        print ">>>" + str(cur_service_k) + " 测试cidata服务",
        app_service_service_config20()
        print " ...ok"
    elif cur_service_k == 21:
        print ">>>" + str(cur_service_k) + " 测试top bar服务",
        app_service_service_config21()
        print " ...ok"
    elif cur_service_k == 22:
        print ">>>" + str(cur_service_k) + " 测试论坛服务",
        app_service_service_config22()
        print " ...ok"
    elif cur_service_k == 23:
        print ">>>" + str(cur_service_k) + " 测试会员服务",
        app_service_service_config23()
        print " ...ok"
    elif cur_service_k == 24:
        print ">>>" + str(cur_service_k) + " 测试互动直播服务",
        app_service_service_config24()
        print " ...ok"
    elif cur_service_k == 25:
        print ">>>" + str(cur_service_k) + " 测试商品服务",
        app_service_service_config25()
        print " ...ok"
    elif cur_service_k == 26:
        print ">>>" + str(cur_service_k) + " 测试orders服务",
        app_service_service_config26()
        print " ...ok"
    elif cur_service_k == 27:
        print ">>>" + str(cur_service_k) + " 测试edu_admin服务",
        app_service_service_config27()
        print " ...ok"
    elif cur_service_k == 28:
        print ">>>" + str(cur_service_k) + " 测试race服务",
        app_service_service_config28()
        print " ...ok"

    # service_num是服务总量, 总共28个服务
    if cur_service_k < service_num:
        #pass
        test_next_service()
    else:
        print " ...ok"
        login_out()
        time.sleep(5)
        quit_firefox()


# "我的应用"->"服务"->"服务说明"
def app_service_service_explanation():
    global cur_service_k
    time.sleep(2)
    driver.find_element_by_css_selector('li.card-auto:nth-child(' + str(cur_service_k) + ') > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > a:nth-child(1)').click()


# "我的应用"->"服务"->"api列表"
def app_service_api_list():
    global cur_service_k
    time.sleep(1)
    #if cur_service_k != 22:
    # 这个界面打开了swagger文档
    driver.find_element_by_css_selector('li.card-auto:nth-child(' + str(cur_service_k) + ') > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > a:nth-child(2)').click()
    # else:
    #     # 打开git lab
    #     driver.find_element_by_css_selector('#user_login').clear()
    #     driver.find_element_by_css_selector('#user_login').send_keys('chenwei90@corp-ci.com')
    #     time.sleep(1)
    #     driver.find_element_by_css_selector('#user_password').clear()
    #     driver.find_element_by_css_selector('#user_password').send_keys('victor1990')
    #     time.sleep(1)
    #     driver.find_element_by_css_selector('.btn-save').click()


# "我的应用"->"服务"->"服务配置"
def app_service_service_config1():
    global cur_service_k

    # 短信模板
    time.sleep(1)
    driver.find_element_by_css_selector("#page-wrapper .form-control").clear()
    driver.find_element_by_css_selector("#page-wrapper .form-control").send_keys(u"短信验证码模版test")

    time.sleep(1)
    driver.find_element_by_css_selector("#page-wrapper .btn-primary").click()   # 保存

    time.sleep(2)
    #driver.switch_to.alert.accept()
    driver.switch_to_alert().accept()

    # 短信模板over, 第三方登录(应用列表+跨域设置+第三方登录)
    time.sleep(2)
    driver.get("http://idg-preprod.tunnel.nibaguai.com/account/main.php?action=third_login.html&appkey=" + appkey)

    # 应用列表
    time.sleep(1)
    driver.find_element_by_css_selector('#side-menu > li:nth-child(1) > a:nth-child(1)').click()

    # 跨域配置
    time.sleep(2)
    driver.find_element_by_css_selector('#side-menu > li:nth-child(2) > a:nth-child(1)').click()

    # 第三方账号配置
    time.sleep(2)
    driver.find_element_by_css_selector('.fa-wechat').click()

    # 保存
    #time.sleep(2)
    #driver.find_element_by_css_selector(".btn-default").click()

    # 返回->我的应用下面
    time.sleep(2)
    driver.find_element_by_css_selector('a.btn').click()

    click_service_btn()


# "我的应用"->"服务"->"用户服务"->"服务配置"->
def app_service_service_config2():
    # 前缀
    time.sleep(1)
    driver.find_element_by_css_selector('input.form-control:nth-child(2)').clear()
    time.sleep(1)
    driver.find_element_by_css_selector('input.form-control:nth-child(2)').send_keys("hello world")

    # 头像地址
    time.sleep(1)
    driver.find_element_by_css_selector('input.form-control:nth-child(5)').clear()
    time.sleep(1)
    driver.find_element_by_css_selector('input.form-control:nth-child(5)').send_keys('a.b.c/avatar.png')

    # 保存
    time.sleep(1)
    driver.find_element_by_css_selector('#page-wrapper > div:nth-child(2) > div.col-lg-12 > form > div > div.row > div > button').click()
    time.sleep(2)
    driver.switch_to.alert.accept()

    time.sleep(2)
    driver.find_element_by_css_selector('#page-wrapper > div:nth-child(1) > div > h1 > div > a').click() # 返回按钮


# 支付服务
def app_service_service_config3():
    # 接入首页
    time.sleep(1)
    driver.find_element_by_css_selector('#side-menu > li:nth-child(1) > a').click()

    # 参数配置->服务商配置
    time.sleep(1)
    driver.find_element_by_css_selector('#side-menu > li:nth-child(2) > ul > li:nth-child(5) > a').click()

    # 参数配置->服务商配置->查看
    time.sleep(1)
    driver.find_element_by_css_selector('#page-wrapper > div.panel-body > div > table > tbody:nth-child(2) > tr > td:nth-child(5) > button').click()

    # 参数配置->服务商配置->查看->编辑
    time.sleep(1)
    driver.find_element_by_css_selector('#page-wrapper > div:nth-child(2) > div.col-lg-6 > form > a').click()

    # 参数配置->服务商配置->服务商名称
    time.sleep(1)
    driver.find_element_by_css_selector('#wxName').clear()
    driver.find_element_by_css_selector('#wxName').send_keys('name')

    # 参数配置->服务商配置->应用APP ID
    time.sleep(1)
    driver.find_element_by_css_selector('#wxAppID').clear()
    driver.find_element_by_css_selector('#wxAppID').send_keys('123456')

    # 参数配置->服务商配置->微信支付商户号
    time.sleep(1)
    driver.find_element_by_css_selector('#wxPayNum').clear()
    driver.find_element_by_css_selector('#wxPayNum').send_keys('abcdefg')

    # 参数配置->服务商配置->微信支付API密钥
    time.sleep(1)
    driver.find_element_by_css_selector('#wxAppSecret').clear()
    driver.find_element_by_css_selector('#wxAppSecret').send_keys('helloworld1')

    # 参数配置->服务商配置->商户证书
    time.sleep(1)
    driver.find_element_by_css_selector('#wxAppCert').clear()
    driver.find_element_by_css_selector('#wxAppCert').send_keys('helloworld2')

    # 参数配置->服务商配置->证书密钥
    time.sleep(1)
    driver.find_element_by_css_selector('#wxAppCertSecret').clear()
    driver.find_element_by_css_selector('#wxAppCertSecret').send_keys('helloworld3')

    # 参数配置->服务商配置->提交
    time.sleep(1)
    driver.find_element_by_css_selector('#form_wx > button').click()

    time.sleep(1)
    driver.switch_to.alert.accept()

    # 参数配置->移动app
    time.sleep(1)
    driver.find_element_by_css_selector('#side-menu > li:nth-child(2) > ul > li:nth-child(1) > a').click()

    # 参数配置->移动app->微信APP支付->编辑
    time.sleep(1)
    driver.find_element_by_css_selector('#page-wrapper > div.panel-body > div > table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(5) > button').click()

    # 参数配置->移动app->微信APP支付->编辑->应用APP ID
    time.sleep(1)
    driver.find_element_by_css_selector('#wxAppID').clear()
    driver.find_element_by_css_selector('#wxAppID').send_keys('123456')

    # 参数配置->移动app->微信APP支付->编辑->微信支付商户号
    time.sleep(1)
    driver.find_element_by_css_selector('#wxPayNum').clear()
    driver.find_element_by_css_selector('#wxPayNum').send_keys('123456')

    # 参数配置->移动app->微信APP支付->编辑->特约商户
    time.sleep(1)
    driver.find_element_by_css_selector('#radio_service').click()

    time.sleep(1)
    driver.find_element_by_css_selector('#wxServiceProvider').find_element_by_xpath("//option[@value='1']").click()

    # 参数配置->移动app->微信APP支付->编辑->普通商户
    time.sleep(1)
    driver.find_element_by_css_selector('#radio_normal').click()

    # 参数配置->移动app->微信APP支付->编辑->微信支付api密钥
    time.sleep(1)
    driver.find_element_by_css_selector('#wxAppSecret').clear()
    driver.find_element_by_css_selector('#wxAppSecret').send_keys('123456')

    # 参数配置->移动app->微信APP支付->编辑->商户证书
    time.sleep(1)
    driver.find_element_by_css_selector('#wxAppCert').clear()
    driver.find_element_by_css_selector('#wxAppCert').send_keys('123456')

    # 参数配置->移动app->微信APP支付->编辑->证书密钥
    time.sleep(1)
    driver.find_element_by_css_selector('#wxAppCertSecret').clear()
    driver.find_element_by_css_selector('#wxAppCertSecret').send_keys('123456')

    # 参数配置->移动app->微信APP支付->编辑->提交
    time.sleep(1)
    driver.find_element_by_css_selector('#form_wx > button').click()

    time.sleep(1)
    driver.switch_to.alert.accept()

    # accept之后, 没有回到xx界面, 需要手动点一下“移动wap”
    # 参数配置->移动wap
    time.sleep(1)
    driver.find_element_by_css_selector('#side-menu > li:nth-child(2) > ul > li:nth-child(2) > a').click()

    # 参数配置->移动wap->支付宝手机网站支付支付->编辑
    time.sleep(1)
    driver.find_element_by_css_selector('#page-wrapper > div.panel-body > div > table > tbody:nth-child(2) > tr > td:nth-child(5) > button').click()

    # 参数配置->移动wap->支付宝手机网站支付支付->编辑->应用ID
    time.sleep(1)
    driver.find_element_by_css_selector('#app_id').clear()
    driver.find_element_by_css_selector('#app_id').send_keys('123456')

    # 参数配置->移动wap->支付宝手机网站支付支付->编辑->商户RSA私钥（PKCS8格式)
    time.sleep(1)
    driver.find_element_by_css_selector('#alipayRSA').clear()
    driver.find_element_by_css_selector('#alipayRSA').send_keys(u'商户RSA私钥')

    # 参数配置->移动wap->支付宝手机网站支付支付->编辑->支付宝公钥
    time.sleep(1)
    driver.find_element_by_css_selector('#alipayKey').clear()
    driver.find_element_by_css_selector('#alipayKey').send_keys(u'支付宝公钥')

    # 参数配置->移动wap->支付宝手机网站支付支付->编辑->提交
    time.sleep(1)
    driver.find_element_by_css_selector('#form_add_alipay > button').click()

    time.sleep(1)
    driver.switch_to.alert.accept()

    # 参数配置->微信公众号
    time.sleep(1)
    driver.find_element_by_css_selector('#side-menu > li:nth-child(2) > ul > li:nth-child(3) > a').click()

    # 参数配置->微信公众号->微信公众号支付/企业打款->编辑
    time.sleep(1)
    driver.find_element_by_css_selector('#page-wrapper > div.panel-body > div > table > tbody:nth-child(2) > tr > td:nth-child(5) > button').click()

    # 参数配置->微信公众号->微信公众号支付/企业打款->应用ID
    time.sleep(1)
    driver.find_element_by_css_selector('#wxAppID').clear()
    driver.find_element_by_css_selector('#wxAppID').send_keys('123456')

    # 参数配置->微信公众号->微信公众号支付/企业打款->微信支付商户号
    time.sleep(1)
    driver.find_element_by_css_selector('#wxPayNum').clear()
    driver.find_element_by_css_selector('#wxPayNum').send_keys('123456')

    # 参数配置->微信公众号->微信公众号支付/企业打款->特约商户
    time.sleep(1)
    driver.find_element_by_css_selector('#form_wx > div:nth-child(3) > div > label:nth-child(2)').click()

    time.sleep(1)
    driver.find_element_by_css_selector('#form_wx > div:nth-child(3) > div > label:nth-child(1)').click()

    # 参数配置->微信公众号->微信公众号支付/企业打款->微信支付API密钥
    time.sleep(1)
    driver.find_element_by_css_selector('#wxAppSecret').clear()
    driver.find_element_by_css_selector('#wxAppSecret').send_keys('abcdefg')

    # 参数配置->微信公众号->微信公众号支付/企业打款->商户证书
    time.sleep(1)
    driver.find_element_by_css_selector('#wxAppCert').clear()
    driver.find_element_by_css_selector('#wxAppCert').send_keys('abcdefg')

    # 参数配置->微信公众号->微信公众号支付/企业打款->证书密钥
    time.sleep(1)
    driver.find_element_by_css_selector('#wxAppCertSecret').clear()
    driver.find_element_by_css_selector('#wxAppCertSecret').send_keys('abcdefg')

    # 参数配置->微信公众号->微信公众号支付/企业打款->提交
    time.sleep(1)
    driver.find_element_by_css_selector('#form_wx > button').click()

    time.sleep(1)
    driver.switch_to.alert.accept()

    # 数据分析->交易额
    time.sleep(1)
    driver.find_element_by_css_selector('#side-menu > li:nth-child(4) > ul > li:nth-child(1) > a').click()

    # 数据分析->交易量
    time.sleep(1)
    driver.find_element_by_css_selector('#side-menu > li:nth-child(4) > ul > li:nth-child(2) > a').click()

    # 数据分析->转化率
    time.sleep(1)
    driver.find_element_by_css_selector('#side-menu > li:nth-child(4) > ul > li:nth-child(3) > a').click()

    # 企业打款->企业打款
    time.sleep(1)
    driver.find_element_by_css_selector('#side-menu > li:nth-child(5) > ul > li:nth-child(1) > a').click()

    # 企业打款->企业打款->打款指南
#    time.sleep(1)
#    driver.find_element_by_css_selector('#page1 > div.pull-right > button').click()

    # 企业打款->企业打款->打款指南->确定
#    time.sleep(1)
#    driver.find_element_by_css_selector('#myModal4 > div > div > div.modal-footer > div > button').click()

    # 企业打款->企业打款->业务转账单号
    time.sleep(1)
    driver.find_element_by_css_selector('#transferId').clear()
    driver.find_element_by_css_selector('#transferId').send_keys('123456')

    # 企业打款->企业打款->收款账户OpenID
    time.sleep(1)
    driver.find_element_by_css_selector('#openId').clear()
    driver.find_element_by_css_selector('#openId').send_keys('123456')

    # 企业打款->企业打款->姓名校验（不校验姓名）
    time.sleep(1)
    driver.find_element_by_css_selector('#page1 > div.row > div > form > div:nth-child(4) > div:nth-child(4) > label').click()

    # 企业打款->企业打款->如选择校验姓名，请填写收款人真实姓名
    time.sleep(1)
    driver.find_element_by_css_selector('#targetName').clear()
    driver.find_element_by_css_selector('#targetName').send_keys(u'陈维')

    # 企业打款->企业打款->转账金额
    time.sleep(1)
    driver.find_element_by_css_selector('#amount').clear()
    driver.find_element_by_css_selector('#amount').send_keys('5000')

    # 企业打款->企业打款->转账描述
    time.sleep(1)
    driver.find_element_by_css_selector('#transferDsc').clear()
    driver.find_element_by_css_selector('#transferDsc').send_keys(u'这是一个转账描述信息')

    # 企业打款->企业打款->创建交易
    time.sleep(1)
    driver.find_element_by_css_selector('#page1 > div.row > div > form > button').click()

    time.sleep(1)
    driver.switch_to.alert.accept()

    # 企业打款->打款查询->打款记录
    time.sleep(1)
    driver.find_element_by_css_selector('#side-menu > li:nth-child(5) > ul > li:nth-child(2) > a').click()

    # 企业打款->打款查询->打款记录->所有打款状态
    time.sleep(1)
    driver.find_element_by_id('state').click()

    # 企业打款->打款查询->打款记录->所有配置渠道
    time.sleep(1)
    driver.find_element_by_id('config_type').click()

    # 企业打款->打款查询->打款记录->时间倒序显示
    time.sleep(1)
    driver.find_element_by_id('order_by').click()

    # 联调工具->交易订单生成
    time.sleep(1)
    driver.find_element_by_css_selector('#side-menu > li:nth-child(6) > ul > li:nth-child(1) > a').click()

    time.sleep(1)
    driver.find_element_by_css_selector('#wrapper > nav > div.header > a').click()

    click_service_btn()

# 实体表格服务, 暂时不管, 听说不用测试
def app_service_service_config4():
    time.sleep(1)
    driver.back()


# 直播
def app_service_service_config5():
    time.sleep(1)
    driver.find_element_by_css_selector('.form-control').clear()
    driver.find_element_by_css_selector('.form-control').send_keys('a.b.c')

    time.sleep(1)
    driver.find_element_by_css_selector('.checkbox > label:nth-child(1) > input:nth-child(1)').click()
    time.sleep(1)
    driver.find_element_by_css_selector('.checkbox > label:nth-child(1) > input:nth-child(1)').click()

    time.sleep(1)
    driver.find_element_by_css_selector('.btn').click()

    time.sleep(2)
    driver.switch_to.alert.accept() # 这句话, 已经回到了服务列表界面


# push
def app_service_service_config6():
    # 基础配置->推送渠道选择->个推
    time.sleep(1)
    driver.find_element_by_css_selector('label.checkbox-inline:nth-child(1)').click()
    time.sleep(1)
    driver.find_element_by_css_selector('label.checkbox-inline:nth-child(1)').click()

    # 基础配置->推送渠道选择->极光
    time.sleep(1)
    driver.find_element_by_css_selector('label.checkbox-inline:nth-child(2)').click()
    time.sleep(1)
    driver.find_element_by_css_selector('label.checkbox-inline:nth-child(2)').click()

    # 基础配置->推送渠道选择->小米
    time.sleep(1)
    driver.find_element_by_css_selector('label.checkbox-inline:nth-child(3)').click()

    # 基础配置->ios APNS选择
    time.sleep(1)
    driver.find_element_by_css_selector('label.radio-inline:nth-child(2) > input:nth-child(1)').click()

    # push 渠道配置(选择极光)
    time.sleep(1)
    driver.find_element_by_css_selector('div.row:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)').click()

    # AppKey
    time.sleep(1)
    driver.find_element_by_css_selector('#jiguang > div:nth-child(2) > input:nth-child(2)').clear()
    driver.find_element_by_css_selector('#jiguang > div:nth-child(2) > input:nth-child(2)').send_keys('123456')

    # Master Secret
    time.sleep(1)
    driver.find_element_by_css_selector('#jiguang > div:nth-child(3) > input:nth-child(2)').clear()
    driver.find_element_by_css_selector('#jiguang > div:nth-child(3) > input:nth-child(2)').send_keys('123456')

    # 应用平台, 选择IOS
    time.sleep(1)
    driver.find_element_by_css_selector('div.row:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)').click()

    # 应用包名
    time.sleep(1)
    driver.find_element_by_css_selector('#iOS > div:nth-child(2) > input:nth-child(2)').clear()
    driver.find_element_by_css_selector('#iOS > div:nth-child(2) > input:nth-child(2)').send_keys('com.ci123.www')

    # 保存按钮
    time.sleep(1)
    driver.find_element_by_css_selector('.btn').click()
    time.sleep(1)
    driver.switch_to.alert.accept()

    # 上面accept之后, 会返回到服务列表界面, 需要再进一次push
    # "服务配置"是第3个按钮
    time.sleep(1)
    driver.find_element_by_css_selector('li.card-auto:nth-child(' + str(cur_service_k) + ') > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > a:nth-child(3)').click()

    # 推送通知
    time.sleep(1)
    driver.find_element_by_css_selector('#side-menu > li:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)').click()

    # 推送通知->通知标题
    time.sleep(1)
    driver.find_element_by_css_selector('div.panel:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)').clear()
    driver.find_element_by_css_selector('div.panel:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)').send_keys('title')

    # 推送通知->通知内容
    time.sleep(1)
    driver.find_element_by_css_selector('div.panel:nth-child(1) > div:nth-child(1) > div:nth-child(2) > textarea:nth-child(2)').clear()
    driver.find_element_by_css_selector('div.panel:nth-child(1) > div:nth-child(1) > div:nth-child(2) > textarea:nth-child(2)').send_keys('notice_content')

    # 推送通知->透传内容
    time.sleep(1)
    driver.find_element_by_css_selector('div.panel:nth-child(1) > div:nth-child(1) > div:nth-child(3) > textarea:nth-child(2)').clear()
    driver.find_element_by_css_selector('div.panel:nth-child(1) > div:nth-child(1) > div:nth-child(3) > textarea:nth-child(2)').send_keys('spread_content')

    # 推送通知->目标平台(选择IOS)
    time.sleep(1)
    driver.find_element_by_css_selector('label.checkbox-inline:nth-child(3)').click()

    # 推送通知->IOS环境(测试环境)
    time.sleep(1)
    driver.find_element_by_css_selector('#ios_sandbox > label:nth-child(3)').click()

    # 推送通知->目标用户类型->全部用户
    time.sleep(1)
    driver.find_element_by_css_selector('div.panel:nth-child(2) > div:nth-child(1) > div:nth-child(3) > label:nth-child(3)').click()

    # 推送通知->目标用户ID/别名/Tag
    time.sleep(1)
    driver.find_element_by_css_selector('div.panel:nth-child(2) > div:nth-child(1) > div:nth-child(4) > input:nth-child(2)').clear()
    driver.find_element_by_css_selector('div.panel:nth-child(2) > div:nth-child(1) > div:nth-child(4) > input:nth-child(2)').send_keys('123456')

    # 推送通知->后续动作->打开指定页面
    time.sleep(1)
    driver.find_element_by_css_selector('div.form-group:nth-child(5) > label:nth-child(3)').click()

    # 推送通知->页面名称
    time.sleep(1)
    driver.find_element_by_css_selector('#open_page > input:nth-child(2)').clear()
    driver.find_element_by_css_selector('#open_page > input:nth-child(2)').send_keys('123456')

    # 页面参数
    time.sleep(1)
    driver.find_element_by_css_selector('textarea.form-control:nth-child(4)').clear()
    driver.find_element_by_css_selector('textarea.form-control:nth-child(4)').send_keys('123456')

    # 推送方式, 选择即时
    time.sleep(1)
    driver.find_element_by_css_selector('div.panel:nth-child(3) > div:nth-child(1) > div:nth-child(1) > label:nth-child(3) > input:nth-child(1)').click()

    # 定时推送时间
    time.sleep(1)
    driver.find_element_by_css_selector('#send_time').clear()
    driver.find_element_by_css_selector('#send_time').send_keys('2017/04/13 15:00:00')

    # 离线消息
    time.sleep(1)
    driver.find_element_by_css_selector('div.panel:nth-child(3) > div:nth-child(1) > div:nth-child(3) > label:nth-child(3)').click()

    # 离线消息有效时长
    time.sleep(1)
    driver.find_element_by_css_selector('div.panel:nth-child(3) > div:nth-child(1) > div:nth-child(4) > input:nth-child(2)').clear()
    driver.find_element_by_css_selector('div.panel:nth-child(3) > div:nth-child(1) > div:nth-child(4) > input:nth-child(2)').send_keys('8')

    # 发送按钮
    time.sleep(1)
    driver.find_element_by_css_selector('.btn').click()

    # 弹框
    time.sleep(1)
    driver.switch_to.alert.accept()

    # 返回主界面
    time.sleep(1)
    driver.find_element_by_css_selector('.header-brand > span:nth-child(2)').click()

    click_service_btn()


# 活动
def app_service_service_config7():
    time.sleep(1)
    driver.find_element_by_css_selector('#test_wx_config').click()

    time.sleep(1)
    driver.switch_to.alert.accept()

    # 返回按钮
    time.sleep(1)
    driver.find_element_by_css_selector('a.btn').click()


# 微官网
def app_service_service_config8():
    time.sleep(2)
    driver.find_element_by_css_selector('#groups-cover-lg > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)').send_keys('/Users/chenwei/Desktop/mac_ip.png')

    time.sleep(1)
    driver.find_element_by_css_selector('#groups-cover-sm > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)').send_keys('/Users/chenwei/Desktop/mac_ip.png')

    time.sleep(1)
    driver.find_element_by_css_selector('#page-cover > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)').send_keys('/Users/chenwei/Desktop/mac_ip.png')

    time.sleep(1)
    driver.find_element_by_css_selector('#share_img > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)').send_keys('/Users/chenwei/Desktop/mac_ip.png')

    # 分享默认标题
    time.sleep(1)
    driver.find_element_by_css_selector('div.form-group:nth-child(9) > input:nth-child(2)').clear()
    driver.find_element_by_css_selector('div.form-group:nth-child(9) > input:nth-child(2)').send_keys('default_title')

    # 分享默认描述
    time.sleep(1)
    driver.find_element_by_css_selector('div.form-group:nth-child(10) > input:nth-child(2)').clear()
    driver.find_element_by_css_selector('div.form-group:nth-child(10) > input:nth-child(2)').send_keys('default_description')

    # time.sleep(1)
    # modal_param_located_in
    # driver.find_element_by_css_selector("select.form-control").find_element_by_xpath("//option[@value='早教行业']").click()

    time.sleep(1)
    driver.find_element_by_css_selector('.btn').click()

    # 弹出框
    time.sleep(1)
    driver.switch_to.alert.accept()


# 预约(点一下就行了, 直接开启)
def app_service_service_config9():
    pass


# 启动页
def app_service_service_config10():
    time.sleep(1)
    driver.switch_to.alert.accept()


# CMS(点一下就行了, 直接开启)
def app_service_service_config11():
    pass


# 微海报
def app_service_service_config12():
    # 选择行业
    time.sleep(2)
    driver.find_element_by_css_selector('select.form-control').find_element_by_xpath("//option[@value='3']").click()

    # 设置品牌宣传语
    time.sleep(1)
    driver.find_element_by_css_selector('div.col-sm-10:nth-child(4) > input:nth-child(1)').clear()
    driver.find_element_by_css_selector('div.col-sm-10:nth-child(4) > input:nth-child(1)').send_keys(u'一站式开发互联网平台')

    # 上传图片
    time.sleep(1)
    driver.find_element_by_css_selector('#update_file').send_keys('/Users/chenwei/Desktop/mac_ip.png')

    # 设置logo跳转链接
    time.sleep(1)
    driver.find_element_by_css_selector('div.col-sm-10:nth-child(8) > input:nth-child(1)').clear()
    driver.find_element_by_css_selector('div.col-sm-10:nth-child(8) > input:nth-child(1)').send_keys('http.weihaibao.com')

    # 设置微信公众号(公众号的app id)
    time.sleep(1)
    driver.find_element_by_css_selector('div.col-sm-10:nth-child(10) > input:nth-child(1)').clear()
    driver.find_element_by_css_selector('div.col-sm-10:nth-child(10) > input:nth-child(1)').send_keys('123456')

    # 设置微信公众号(公众号的App secret)
    time.sleep(1)
    driver.find_element_by_css_selector('input.form-control:nth-child(3)').clear()
    driver.find_element_by_css_selector('input.form-control:nth-child(3)').send_keys(appsecret)

    # 保存修改
    time.sleep(1)
    driver.find_element_by_css_selector('button.btn').click()

    # 弹出框
    time.sleep(1)
    driver.switch_to.alert.accept()


# 代理
def app_service_service_config13():
    if False:
        # 添加客户APP
        time.sleep(1)
        driver.find_element_by_css_selector('#add-btn').click()

        # 添加业务APP名称
        time.sleep(1)
        driver.find_element_by_css_selector('input.form-control:nth-child(2)').clear()
        driver.find_element_by_css_selector('input.form-control:nth-child(2)').send_keys('app_name')

        # 添加业务AppKey
        time.sleep(1)
        driver.find_element_by_css_selector('#client_appkey').clear()
        driver.find_element_by_css_selector('#client_appkey').send_keys(appkey)

        # 添加AppSecret
        time.sleep(1)
        driver.find_element_by_css_selector('#client_appsecret').clear()
        driver.find_element_by_css_selector('#client_appsecret').send_keys(appsecret)

        # 添加按钮
        time.sleep(1)
        driver.find_element_by_css_selector('#add-modal > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)')
        driver.find_element_by_css_selector('#add-submit').click()

        # 弹框 (这边会提示: APP不能代理自己)
        time.sleep(1)
        driver.switch_to.alert.accept()

        # 所以暂时取消掉
        time.sleep(1)
        driver.find_element_by_css_selector('#add-modal > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)')

    # 这边有个bug, 右上角的返回按钮不能点(点了没反应), 所以通过左上角的"智慧中台"按钮返回
    time.sleep(1)
    driver.find_element_by_css_selector('.header-brand').click()

    click_service_btn()


# 权限管理(不用管, 点一下就行了)
def app_service_service_config14():
    # 弹出框
    time.sleep(1)
    driver.switch_to.alert.accept()


# api-tool (和"我的应用->开发"是一样的, 直接调这个方法即可)
def app_service_service_config15():
    app_develop()


# 积分商城
def app_service_service_config16():
    # 基础配置->积分商城默认标题
    time.sleep(1)
    driver.find_element_by_css_selector('div.form-group:nth-child(1) > input:nth-child(2)').clear()
    driver.find_element_by_css_selector('div.form-group:nth-child(1) > input:nth-child(2)').send_keys('credit_shop_title')

    # 基础配置->默认登陆链接
    time.sleep(1)
    driver.find_element_by_css_selector('div.form-group:nth-child(2) > input:nth-child(2)').clear()
    driver.find_element_by_css_selector('div.form-group:nth-child(2) > input:nth-child(2)').send_keys('credit_shop_link')

    # 基础配置->保存
    time.sleep(1)
    driver.find_element_by_css_selector('.btn').click()

    # 弹出框
    time.sleep(1)
    driver.switch_to.alert.accept()

    # 从基础配置->积分配置
    time.sleep(1)
    driver.find_element_by_css_selector('#side-menu > li:nth-child(2) > a:nth-child(1)').click()

    # 积分配置->积分来源选择->外部
    time.sleep(1)
    driver.find_element_by_css_selector('label.radio-inline:nth-child(1)').click()

    # 积分配置->积分来源选择->中台
    time.sleep(1)
    driver.find_element_by_css_selector('label.radio-inline:nth-child(2)').click()

    # 积分1单位名称
    time.sleep(1)
    driver.find_element_by_css_selector('div.panel-body:nth-child(2) > div:nth-child(1) > input:nth-child(2)').clear()
    driver.find_element_by_css_selector('div.panel-body:nth-child(2) > div:nth-child(1) > input:nth-child(2)').send_keys('123456')

    # 积分2单位名称
    time.sleep(1)
    driver.find_element_by_css_selector('div.panel-body:nth-child(3) > div:nth-child(1) > input:nth-child(2)').clear()
    driver.find_element_by_css_selector('div.panel-body:nth-child(3) > div:nth-child(1) > input:nth-child(2)').send_keys('abcdefg')

    # 保存
    time.sleep(1)
    driver.find_element_by_css_selector('.btn').click()

    # 弹出框
    time.sleep(1)
    driver.switch_to.alert.accept()

    # 订单相关配置
    time.sleep(1)
    driver.find_element_by_css_selector('#side-menu > li:nth-child(3) > a:nth-child(1)').click()

    # 订单相关配置->订单审核模式->无审核
    time.sleep(1)
    driver.find_element_by_css_selector('label.radio-inline:nth-child(2)').click()

    # 订单相关配置->订单短信提醒
    time.sleep(1)
    driver.find_element_by_css_selector('.form-control').clear()
    driver.find_element_by_css_selector('.form-control').send_keys(u'这是一个模板')

    # 保存按钮
    time.sleep(1)
    driver.find_element_by_css_selector('#page-wrapper > div > div.row > div > form > div > button').click()

    # 弹出框
    time.sleep(1)
    driver.switch_to.alert.accept()

    # 返回服务列表界面
    time.sleep(1)
    driver.find_element_by_css_selector('#wrapper > nav > div.header > a').click()

    click_service_btn()


# 官网
def app_service_service_config17():
    # 下拉列表, 选择直播
    time.sleep(1)
    driver.find_element_by_css_selector('.form-control').find_element_by_xpath("//option[@value='/live/main.php?action=admin_index.html']").click()

    # 保存按钮
    time.sleep(1)
    driver.find_element_by_css_selector('.btn').click()

    # 弹出框
    time.sleep(1)
    #driver.switch_to.alert.accept()
    driver.switch_to_alert().accept()

    # TODO back to 服务, 不是列表
    time.sleep(2)
    driver.find_element_by_css_selector('.header-brand').click()
    click_service_btn()


# 商城(开启一下就可以了)
def app_service_service_config18():
    pass


# 微信公众号托管
def app_service_service_config19():
    # AppID
    time.sleep(1)
    driver.find_element_by_css_selector('div.form-group:nth-child(1) > input:nth-child(2)').clear()
    driver.find_element_by_css_selector('div.form-group:nth-child(1) > input:nth-child(2)').send_keys('123456')

    # AppSecret
    time.sleep(1)
    driver.find_element_by_css_selector('div.form-group:nth-child(2) > input:nth-child(2)').clear()
    driver.find_element_by_css_selector('div.form-group:nth-child(2) > input:nth-child(2)').send_keys(appsecret)

    # Token
    time.sleep(1)
    driver.find_element_by_css_selector('div.form-group:nth-child(3) > input:nth-child(2)').clear()
    driver.find_element_by_css_selector('div.form-group:nth-child(3) > input:nth-child(2)').send_keys('123456')

    # Key
    time.sleep(1)
    driver.find_element_by_css_selector('div.form-group:nth-child(4) > input:nth-child(2)').clear()
    driver.find_element_by_css_selector('div.form-group:nth-child(4) > input:nth-child(2)').send_keys('123456')

    # 回调地址
    time.sleep(1)
    driver.find_element_by_css_selector('div.form-group:nth-child(5) > input:nth-child(2)').clear()
    driver.find_element_by_css_selector('div.form-group:nth-child(5) > input:nth-child(2)').send_keys('123456')

    # 退订
    time.sleep(1)
    driver.find_element_by_css_selector('.radio > label:nth-child(2) > input:nth-child(1)').click()

    # 保存按钮
    time.sleep(1)
    driver.find_element_by_css_selector('#create').click()

    # 弹出框
    time.sleep(1)
    driver.switch_to.alert.accept()


# ci data
def app_service_service_config20():
    # 概况->实时统计
    #time.sleep(5)
    #driver.find_element_by_css_selector('#realtimeSummary').click()

    # 概况->实时统计->新增用户
    time.sleep(6)
    driver.find_element_by_css_selector('#body > div > div > div > div > ul > li.active > a').click()

    # 概况->实时统计->时段累计日活
    time.sleep(6)
    driver.find_element_by_css_selector('#body > div > div > div > div > ul > li.active > a').click()

    # 概况->整体趋势
    time.sleep(6)
    driver.find_element_by_css_selector('#trendSummary').click()

    # 用户细查
    time.sleep(6)
    driver.find_element_by_css_selector('#userInsightQuery').click()

    # 用户细查->输入框
    time.sleep(3)
    driver.find_element_by_css_selector('#page-wrapper > div > div:nth-child(2) > div > div > input').clear()
    driver.find_element_by_css_selector('#page-wrapper > div > div:nth-child(2) > div > div > input').send_keys('123456')

    # 用户细查->搜索按钮
    time.sleep(2)
    driver.find_element_by_css_selector('#page-wrapper > div > div:nth-child(2) > div > div > div > button').click()

    # 设置->自定义事件模板
    time.sleep(5)
    driver.find_element_by_css_selector('#customEventTemplate').click()

    # 设置->自定义事件模板->添加模板
    time.sleep(5)
    driver.find_element_by_css_selector('#page-wrapper > div > div:nth-child(3) > div > div > div.panel-heading > button').click()

    # 设置->自定义事件模板->添加模板->事件ID
    time.sleep(1)
    driver.find_element_by_css_selector(
        '#page-wrapper > div > div:nth-child(4) > div > div > div.el-dialog__body > form > div:nth-child(1) > div > div > input').clear()
    driver.find_element_by_css_selector(
        '#page-wrapper > div > div:nth-child(4) > div > div > div.el-dialog__body > form > div:nth-child(1) > div > div > input').send_keys('123456')

    # 设置->自定义事件模板->添加模板->标题模板
    time.sleep(1)
    driver.find_element_by_css_selector(
        '#page-wrapper > div > div:nth-child(4) > div > div > div.el-dialog__body > form > div:nth-child(2) > div > div > input').clear()
    driver.find_element_by_css_selector(
        '#page-wrapper > div > div:nth-child(4) > div > div > div.el-dialog__body > form > div:nth-child(2) > div > div > input').send_keys('title')

    # 设置->自定义事件模板->添加模板->详情模板
    time.sleep(1)
    driver.find_element_by_css_selector(
        '#page-wrapper > div > div:nth-child(4) > div > div > div.el-dialog__body > form > div:nth-child(3) > div > div > textarea').clear()
    driver.find_element_by_css_selector(
        '#page-wrapper > div > div:nth-child(4) > div > div > div.el-dialog__body > form > div:nth-child(3) > div > div > textarea').send_keys('description')

    # 设置->自定义事件模板->添加模板->确定
    time.sleep(1)
    driver.find_element_by_css_selector(
        '#page-wrapper > div > div:nth-child(4) > div > div > div.el-dialog__footer > span > button.el-button.el-button--primary').click()

    # 设置->自定义事件模板->编辑按钮
    time.sleep(1)
    driver.find_element_by_css_selector(
        '#page-wrapper > div > div:nth-child(3) > div > div > div.panel-body > div > div.el-table__body-wrapper > table > tbody > tr > td.el-table_1_column_10 > div > button.el-button.el-button--primary.el-button--small').click()

    # 设置->自定义事件模板->编辑模板->标题模板
    time.sleep(1)
    driver.find_element_by_css_selector(
        '#page-wrapper > div > div:nth-child(4) > div > div > div.el-dialog__body > form > div:nth-child(2) > div > div > input').clear()
    driver.find_element_by_css_selector(
        '#page-wrapper > div > div:nth-child(4) > div > div > div.el-dialog__body > form > div:nth-child(2) > div > div > input').send_keys('title2')

    # 设置->自定义事件模板->编辑模板->详情模板
    time.sleep(1)
    driver.find_element_by_css_selector(
        '#page-wrapper > div > div:nth-child(4) > div > div > div.el-dialog__body > form > div:nth-child(3) > div > div > textarea').clear()
    driver.find_element_by_css_selector(
        '#page-wrapper > div > div:nth-child(4) > div > div > div.el-dialog__body > form > div:nth-child(3) > div > div > textarea').send_keys('description2')

    # 设置->自定义事件模板->编辑模板->确定按钮
    time.sleep(1)
    driver.find_element_by_css_selector('#page-wrapper > div > div:nth-child(4) > div > div > div.el-dialog__footer > span > button.el-button.el-button--primary').click()

    # 设置->自定义事件模板->删除按钮
    time.sleep(1)
    driver.find_element_by_css_selector('#page-wrapper > div > div:nth-child(3) > div > div > div.panel-body > div > div.el-table__body-wrapper > table > tbody > tr > td.el-table_1_column_10 > div > button.el-button.el-button--danger.el-button--small').click()

    # 设置->自定义时间模板->删除->确定按钮
    time.sleep(1)
    driver.find_element_by_css_selector('body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--primary').click()

    # 左上角的返回
    time.sleep(2)
    driver.find_element_by_css_selector('#app > nav > div.header > a').click()

    click_service_btn()


# top bar
def app_service_service_config21():
    # time.sleep(2)
    # driver.find_element_by_css_selector('#head-icon').send_keys('/Users/chenwei/Desktop/mac_ip.png')

    time.sleep(1)
    driver.find_element_by_css_selector('#left-first-menu-1 > a:nth-child(1)').click()
    # 公众号管理->编辑一级目录->目录名称
    time.sleep(1)
    driver.find_element_by_css_selector('#edit-first-menu-name').clear()
    driver.find_element_by_css_selector('#edit-first-menu-name').send_keys(u'公众号管理_modify')

    # 公众号管理->编辑一级目录->链接地址
    # time.sleep(1)
    # driver.find_element_by_css_selector('#edit-first-menu-link').find_element_by_xpath('//option[@value="#"]').click()

    # 公众号管理->编辑一级目录->选择目录类型
    time.sleep(1)
    driver.find_element_by_css_selector('#edit-first-menu-type').find_element_by_xpath("//option[@id='edit-first-type-left']").click()

    # 公众号管理->编辑一级目录->在此目录下建立二级目录
    time.sleep(1)
    driver.find_element_by_css_selector('#edit-first-menu-allow').find_element_by_xpath("//option[@id='edit-first-allow-no']").click()

    # 公众号管理->编辑一级目录->移动位置
    time.sleep(1)
    driver.find_element_by_css_selector('#edit-first-menu-left').click()

    # 公众号管理->编辑一级目录->取消修改
    time.sleep(1)
    driver.find_element_by_css_selector('#edit_first_menu > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(3)').click()

    # 微海报
    time.sleep(1)
    driver.find_element_by_css_selector('#left-first-menu-2 > a:nth-child(1)').click()

    # 微海报->编辑一级目录->目录名称
    time.sleep(1)
    driver.find_element_by_css_selector('#edit-first-menu-name').clear()
    driver.find_element_by_css_selector('#edit-first-menu-name').send_keys(u'微海报_modify')

    # 微海报->编辑一级目录->选择目录类型
    time.sleep(1)
    driver.find_element_by_css_selector('#edit-first-menu-type').find_element_by_xpath("//option[@id='edit-first-type-left']").click()

    # 微海报->编辑一级目录->在此目录下建立二级目录
    time.sleep(1)
    driver.find_element_by_css_selector('#edit-first-menu-allow').find_element_by_xpath("//option[@id='edit-first-allow-no']").click()

    # 微海报->编辑一级目录->移动位置
    time.sleep(1)
    driver.find_element_by_css_selector('#edit-first-menu-left').click()

    # 微海报->编辑一级目录->取消修改
    time.sleep(1)
    driver.find_element_by_css_selector('#edit_first_menu > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(3)').click()

    # 官网组件管理
    time.sleep(1)
    driver.find_element_by_css_selector('#left-first-menu-4 > a:nth-child(1) > span:nth-child(1)').click()

    # 官网组件管理->添加分类
    time.sleep(1)
    driver.find_element_by_css_selector('#left-first-menu-cate-4').click()

    # 添加分类
    time.sleep(1)
    driver.find_element_by_css_selector('#add-category-name').clear()
    driver.find_element_by_css_selector('#add-category-name').send_keys('category')

    # 取消掉
    time.sleep(1)
    driver.find_element_by_css_selector('#new-category > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(2)').click()

    # 添加一级目录
    time.sleep(2)
    driver.find_element_by_css_selector('#new_first_a').click()

    # 添加一级目录->目录名称
    time.sleep(1)
    driver.find_element_by_css_selector('#first-menu-name').clear()
    driver.find_element_by_css_selector('#first-menu-name').send_keys('dir_name')

    # 添加一级目录->链接地址
    time.sleep(1)
    driver.find_element_by_css_selector('#first-menu-link').find_element_by_xpath('//option[@value="/splash/main.php?action=index.html"]').click()

    # 添加一级目录->选择目录类型
    time.sleep(1)
    driver.find_element_by_css_selector('#first-menu-type').find_element_by_xpath("//option[@value='left']").click()

    # 添加一级目录->在此目录下建立二级目录
    time.sleep(1)
    driver.find_element_by_css_selector('#first-menu-allow-second').find_element_by_xpath("//option[@value='yes']").click()

    # 添加一级目录->取消修改
    time.sleep(1)
    driver.find_element_by_css_selector('#new_first_menu > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)').click()

    # 链接管理!!!!!!!
    time.sleep(2)
    driver.find_element_by_css_selector('.nav-second-level > li:nth-child(2) > a:nth-child(1)').click()

    # 链接管理->"新增外部链接"按钮
    time.sleep(1)
    driver.find_element_by_css_selector('button.btn-primary:nth-child(1)').click()

    # 新增外部链接->链接名称
    time.sleep(1)
    driver.find_element_by_css_selector('#add-link-modal > div:nth-child(1) > div:nth-child(1) > form:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)').clear()
    driver.find_element_by_css_selector('#add-link-modal > div:nth-child(1) > div:nth-child(1) > form:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)').send_keys('a.b.com')

    # 新增外部链接->链接URL
    time.sleep(1)
    driver.find_element_by_css_selector('.input-inline > select:nth-child(1)').find_element_by_xpath('//option["https://"]').click()

    # 确认添加
    time.sleep(1)
    driver.find_element_by_css_selector('#add-link-modal > div:nth-child(1) > div:nth-child(1) > form:nth-child(2) > div:nth-child(2) > button:nth-child(1)').click()

    # 左上角的返回
    time.sleep(2)
    driver.find_element_by_css_selector('#wrapper > nav:nth-child(1) > div:nth-child(1) > a:nth-child(1)').click()

    time.sleep(1)
    click_service_btn()


# 论坛
def app_service_service_config22():
    pass


# 会员
def app_service_service_config23():
    pass


# 互动直播
def app_service_service_config24():
    # app_logo
    # time.sleep(2)
    # driver.find_element_by_id('update_file').send_keys('/Users/chenwei/Desktop/mac_ip.png')

    # app 名称
    time.sleep(1)
    driver.find_element_by_css_selector('div.form-group:nth-child(2) > input:nth-child(2)').clear()
    driver.find_element_by_css_selector('div.form-group:nth-child(2) > input:nth-child(2)').send_keys(u'互动直播_modify')

    # 一句广告话
    time.sleep(1)
    driver.find_element_by_css_selector('div.form-group:nth-child(3) > input:nth-child(2)').clear()
    driver.find_element_by_css_selector('div.form-group:nth-child(3) > input:nth-child(2)').send_keys(u'description')

    # 产品展示图
    # time.sleep(1)
    # driver.find_element_by_css_selector('#show_img').send_keys('/Users/chenwei/Desktop/test.jpg')

    # IOS 下载
    time.sleep(1)
    driver.find_element_by_css_selector('div.form-group:nth-child(5) > input:nth-child(2)').clear()
    driver.find_element_by_css_selector('div.form-group:nth-child(5) > input:nth-child(2)').send_keys(u'IOS下载地址')

    # IOS Scheme
    time.sleep(1)
    driver.find_element_by_css_selector('div.form-group:nth-child(6) > input:nth-child(2)').clear()
    driver.find_element_by_css_selector('div.form-group:nth-child(6) > input:nth-child(2)').send_keys('123456')

    # 安卓下载
    time.sleep(1)
    driver.find_element_by_css_selector('div.form-group:nth-child(7) > input:nth-child(2)').clear()
    driver.find_element_by_css_selector('div.form-group:nth-child(7) > input:nth-child(2)').send_keys(u'Android下载地址')

    # Android Scheme
    time.sleep(1)
    driver.find_element_by_css_selector('div.form-group:nth-child(8) > input:nth-child(2)').clear()
    driver.find_element_by_css_selector('div.form-group:nth-child(8) > input:nth-child(2)').send_keys('123456')

    # 保存按钮
    time.sleep(1)
    driver.find_element_by_css_selector('#submitForm').click()

    alert_accept()
    time.sleep(3)
    close_label()

    # 用户协议
    time.sleep(1)
    driver.find_element_by_css_selector('#side-menu > li:nth-child(2) > a:nth-child(1)').click()
    # 用户协议->APP名称
    time.sleep(1)
    driver.find_element_by_css_selector('#name').clear()
    driver.find_element_by_css_selector('#name').send_keys('aaaaaaa')
    # 用户协议->保存
    time.sleep(1)
    driver.find_element_by_css_selector('.btn').click()
    # 保存后, 有个确定弹出框
    alert_accept()

    # 课程须知
    time.sleep(1)
    driver.find_element_by_css_selector('#side-menu > li:nth-child(3) > a:nth-child(1)')
    # 课程须知->课程须知
    time.sleep(1)
    driver.find_element_by_css_selector('#editor').clear()
    driver.find_element_by_css_selector('#editor').send_keys('course course course')

    # 课程须知->保存按钮
    time.sleep(1)
    driver.find_element_by_css_selector('.btn').click()

    # 同上
    alert_accept()

    # 返回主界面
    time.sleep(2)
    driver.find_element_by_css_selector('.header-brand').click()

    time.sleep(1)
    click_service_btn()


# 商品
def app_service_service_config25():
    pass


# orders
def app_service_service_config26():
    pass


# edu_admin
def app_service_service_config27():
    alert_accept()
    time.sleep(1)
    click_service_btn()


# race
def app_service_service_config28():
    alert_accept()
    time.sleep(1)
    click_service_btn()


# "我的应用"->"服务"->"开启服务"(有的开了,有的没开)
def open_service():
    time.sleep(1)
    driver.find_element_by_css_selector("#page-wrapper .form-control").send_keys("a.b.c")

    time.sleep(1)
    driver.find_element_by_css_selector("#page-wrapper .btn-primary").click()


def click_service_btn():
    # 对于每个服务下面的每个, 每个按钮, 测一遍
    # "服务"是第三个按钮, 所以nth-child(3)
    time.sleep(1)
    driver.find_element_by_css_selector("a[href*=" + appkey + "].bt:nth-child(3)").click()


# 关闭当前标签页, 回到之前界面
def close_label():
    global all_h, cur_h

    all_h = driver.window_handles
    cur_h = driver.current_window_handle

    # 遍历所有标签页, 进行切换
    for k in all_h:
        if k != cur_h:
            driver.switch_to_window(k)
            break

    # 关闭新打开的标签页
    driver.close()
    # 切回到主界面, 否则元素会找不到
    driver.switch_to.window(cur_h)


# 弹出框确认按钮
def alert_accept():
    time.sleep(1)
    driver.switch_to.alert.accept()


# 弹出框取消按钮
def alert_dismiss():
    time.sleep(1)
    driver.switch_to.alert.dismiss()


# 执行js脚本
def exec_js():
    # TODO 1 调用webdriver自带的execute_script()方法
    # TODO 2 这个主要是为了弹出框所用
    pass


# 获得当前时间
def get_current_time():
    return time.time()


# 自动打开浏览器
def open_firefox():
    global driver
    driver = webdriver.Chrome()
    #driver = webdriver.Firefox()
    driver._is_remote = False

    # 窗口最大化, 否则不能切换tab标签, 奇怪
    driver.maximize_window()
    driver.get("http://idg-preprod.tunnel.nibaguai.com/")

    click_login()


# 退出浏览器
def quit_firefox():
    driver.quit()


# 格式化输出
def echo_tab():
    time.sleep(4)
    print "@@@@@@@@@@   echo tab start  @@@@@@@@@@"
    global all_h, cur_h
    all_h = driver.window_handles
    cur_h = driver.current_window_handle
    print ">>>>>>>>所有标签页: ", all_h
    print ">>>>>>>>当前标签为", cur_h
    print "@@@@@@@@@@   echo tab over   @@@@@@@@@@ \n\n"


if __name__ == "__main__":
    commonfunc = CommonFuncs()
    if not commonfunc.check_file_exists('PhoneNum.txt'):
        commonfunc.write_file('PhoneNum.txt', '13900000000')

    start_time = get_current_time()
    open_firefox()
    end_time = get_current_time()
    print "总共执行时间: " + str(end_time - start_time) + "s"