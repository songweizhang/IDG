# -*- coding: utf-8 -*-

import random
import os
import urllib
import urllib2
import json
import string
import socket
import subprocess
# 邮件模块
import smtplib
from email.mime.text import MIMEText
from email.header import Header

error_count = 0
post_count = 0

prefixurl = []
allserver = []

cur_prefix_idx = 0
cur_server_idx = 0

prefixdict = {
    'account': "account",
    'admin': "admin",
    'agent': "agent",
    'channel-user': "channel-user",
    'cms': "cms",
    'cidata': "cidata",
    'hd': "hd",
    'live': "live",
    'pay': "pay",
    'push': "push",
    'shop': "shop",
    'splash': "splash",
    'ucenter': "ucenter",
    'utemplate': "utemplate",
    #'word': "word"
}

reqdict = {
    'account': {
        '/json/bind/phone': ['POST', {
            'appkey': 'appkey_test',
            'token': 'token_test',
            'phone': '13900000000',
            'catpcha': 'catpcha_test'
        }],
        '/json/bind/third': ['POST', {
            'appkey': 'appkey_test',
            'token': 'token',
            'third_appid': 'third_test',
            'access_token': 'access_test',
            'openid': 'openid_test',
            'nickname': 'nickname_test',
            'account_type': 'qq'
        }],
        '/json/unbind': ["POST", {
            'appkey': 'appkey_test',
            'token': 'token_test',
            'account_type': 'phone'
        }],
        '/json/bind/info': ["POST", {
            'appkey': 'appkey_test',
            'token': 'token_test'
        }],
        '/json/login/phone': ["POST", {
            'appkey': 'appkey_test',
            'phone': '13900000000'
        }],
        '/json/login/device': ["POST", {
            'appkey': 'appkey_test',
            'deviceid': 'deviceid_test',
            'platform': 'iOS'
        }],
        '/json/login/third': ["POST", {
            'appkey': 'appkey_test',
            'third_appid': 'third_test',
            'access_token': 'access_test',
            'openid': 'openid_test',
            'nickname': 'nickname_test',
            'account_type': 'qq'
        }],
        '/json/login/auto': ["POST", {
            'appkey': 'appkey_test',
            'token': 'token_test'
        }],
        '/json/login/check': ["POST", {
            'appkey': 'appkey_test',
            'token': 'token_test'
        }],
        '/json/login/kick': ["POST", {
            'appkey': 'appkey_test',
            'token': 'token_test'
        }],
        '/json/change_password/phone': ["POST", {
            'appkey': 'appkey_test',
            'phone': '13900000000',
            'capatcha': 'capatcha_test',
            'password': 'pwd',
            'confirm_password': 'pwd'
        }],
        '/json/captcha/phone': ["POST", {
            'appkey': 'appkey_test',
            'phone': '13900000000'
        }],
        '/json/register/phone': ["POST", {
            'appkey': 'appkey_test',
            'phone': '13900000000',
            'captcha': 'captcha_test',
            'password': 'pwd',
            'confirm_password': 'pwd'
        }],
        '/rpc/register/phone.json': ["POST", {
            'appkey': 'appkey_test',
            'phone': '13900000000',
            'password': 'pwd',
            'token': 'token_test'
        }]
    },
    'admin': {
        '/json/rpc/make_token': ["POST", {
            'username': 'usrname',
            'password': 'pwd',
            'appkey': 'appkey_test',
            'data': 'data_test'
        }],
        '/json/rpc/add_channel': ["POST", {
            'appkey': 'appkey_test',
            'token': 'token_test',
            'name': 'name_test',
            'owner': 'owner_test',
            'owner_name': 'owner_name_test'
        }]
    },
    'channel-user': {
        '/json/rpc/add_user': ["POST", {
            'appkey': 'appkey_test',
            'token': 'token_test',
            'account_id': 'account_test',
            'channel': 'channel_test'
        }],
        '/json/users/login_channel': ["POST", {
            'appkey': 'appkey_test',
            'phone': '13900000000'
        }],
        '/json/users/apply_channel': ["POST", {
            'appkey': 'appkey_test',
            'owner': 'owner_test',
            'owner_name': 'owner_name_test',
            'name': 'name_test'
        }],
        '/json/users/check_channel': ["POST", {
            'appkey': 'appkey_test',
            'phone': '13900000000'
        }]
    },
    'cidata': {
        '/json/dailyAlive': ["GET", {
            'appkey': 'appkey_test',
            'date': '2016-11-11',
            'sign': 'sign_test'
        }]
    },
    'cms': {
        '/json/article/getCateArticle/category_id/article_num/appkey/channel/page/substrcount/dateshowed': ["GET", {

        }],
        '/josn/article/getChannelArticleWithID/appkey/channel/number/limit/cms_flag/cms_article_flag/articleCategoryIndex/subcount': ["GET", {

        }],
        '/json/article/getSameTagArticle/appkey/channel/limit/articleID': ["GET", {

        }],
        '/json/category/listArr/channel/appkey': ["GET", {

        }],
        '/json/article/getNewestArticle/appkey/channel/page/limit/substrcount/showedtime': ["GET", {

        }],
        '/json/article/getArticleByCondition/appkey/channel/search_column/search_orders/search_page': ["GET", {

        }],
        '/json/article/getArticleByCondition/appkey/channel/search_columns/search_page': ["GET", {

        }],
        '/json/carouselfigure/getCarousel/appkey/channel': ["GET", {

        }]
    },
    'hd': {
        '?action=index.html&fwargs[add_myact]=index.html,var_urls,add_myact,': ["GET", {
            'appkey': 'appkey_test',
            'channel': 'channel_test',
            'add_id': '123456'
        }],
        '?action=open.html': ["GET", {
            'appkey': 'appkey_test'
        }],
        '?action=myact.html&fwargs[publish_act]=myact.html,var_acttpls,publish_act': ["GET", {
            'appkey': 'appkey_test',
            'channel': 'channel_test',
            'act_id': 123456
        }],
        '?action=myact.html&fwargs[delete_url]=myact.html,var_acttpls,delete_url,': ["GET", {
            'appkey': 'appkey_test',
            'channel': 'channel_test',
            'act_id': 123456
        }],
        '?action=myact.html&fwargs[reward_list]=myact.html,var_acttpls,reward_list,': ["GET", {
            'appkey': 'appkey_test',
            'channel': 'channel_test',
            'act_id': 123456
        }]
    },
    'live': {
        '/common/live/getSpeak.json': ["GET", {
            'liveId': 123456,
            'lastTime': 123456,
            'order': "desc"
        }],
        '/common/live/getComment.json': ['GET', {
            'liveId': 123456,
            'dated': 123456,
            'orderDesc': 1
        }],
        '/common/live/addComment.json': ["POST", {
            'userId': 123456,
            'liveId': 123456,
            'content': "content_test",
            'type': "type_test",
            'isQuestion': True
        }],
        '/common/live/removeSpeak.json': ["POST", {
            'speakId': 123456
        }],
        '/common/live/createGroup.json': ["POST", {
            'name': 'name_test'
        }],
        '/common/live/addTheme.json': ["POST", {
            'title': 'title_test',
            'startTime': 123456
        }],
        '/common/live/endLive.json': ["POST", {
            'topicId': 123456
        }],
        '/common/live/getInviteWxSDK.json': ["POST", {
            'linkKey': 'linkKey_test'
        }],
        '/common/live/modify.json': ["POST", {
            'type': 'type_test',
            'linkKey': 'key_test',
            'value': 'value_test'
        }],
        '/common/live/saveFocus.json': ["POST", {
            'linkKey': 'key_test',
            'cancelFlag': True
        }],
        #'/common/live/getQrcode.json': ["POST", {
        #    'url': 'url_test'
        #}],
        '/common/live/modifyQrCode.json': ["POST", {
            'liveId': 123456,
            'qrCode': 'code_test',
            'wx_nickname': 'name_test'
        }],
        '/common/live/updateBlackList.json': ["POST", {
            'liveId': 123456,
            'userId': 123456
        }],
        '/common/live/forbidComment.json': ["POST", {
            'liveId': 123456,
            'action': 'action_test'
        }],
        '/common/live/editIntro.json': ["POST", {
            'linkKey': 'link_test',
            'theme': 'theme_test',
            'startTime': 123456,
            'guestName': 'name_test',
            'themeIntro': 'intro_test',
            'guestIntro': 'intro_test'
        }],
        '/common/live/getAllTopics.json': ["GET", {
            'appKey': '123456'
        }],
        '/common/live/getTopicsByIds.json': ["GET", {
            'id': 123456
        }],
        #'/imgUpload.php/upload.json': ["GET", {
        #}],
        #'/imgUpload/uploadFile.json': ["POST", {
        #    'file': 'file_test'
        #}],
        #'/Jssdk/getSignPackage.json': ["POST", {
        #}]
     },
     'pay': {
        '/json/trade/createWeixinMobileTrade': ["POST", {
            'app_key': 'key_test',
            'subject': 'subject_test',
            'detail':  'detail_test',
            'total_fee': 123456,
            'client_ip': 'ip_test',
            'notify_url': 'url_test',
            'out_trade_no': 'trade_test',
            'sign': 'sign_test'
        }],
        '/json/trade/createWeixinJSTrade': ["POST", {
            'app_key': 'key_test',
            'subject': 'subject_test',
            'detail': 'detail_test',
            'total_fee': 123456,
            'client_ip': 'client_test',
            'notify_url': 'url_test',
            'out_trade_no': 'trade_test',
            'openid': 'openid_test',
            'sign': 'sign_test'
        }],
        '/json/trade/createWeixinNativeTrade': ["POST", {
            'app_key': 'key_test',
            'subject': 'subject_test',
            'detail': 'detail_test',
            'total_fee': 123456,
            'client_ip': 'ip_test',
            'notify_url': 'url_test',
            'out_trade_no': 'trade_test',
            'product_id': 'product_test',
            'sign': 'sign_test'
        }],
        '/json/trade/createAlipayMobileTrade': ["POST", {
            'app_key': 'key_test',
            'subject': 'subject_test',
            'detail': 'detail_test',
            'total_fee': 123456,
            'client_ip': 'ip_test',
            'notify_url': 'url_test',
            'out_trade_no': 'trade_test',
            'sign': 'sign_test'
        }],
        '/json/trade/createAlipayDirectTrade': ["POST", {
            'app_key': 'key_test',
            'subject': 'subject_test',
            'detail': 'detail_test',
            'total_fee': 123456,
            'client_ip': 'client_test',
            'notify_url': 'url_test',
            'out_trade_no': 'trade_test',
            'return_url': 'url_test',
            'sign': 'sign_test'
        }],
        '/json/trade/queryTrade': ["POST", {
            'app_key': 'key_test',
            'trade_no': 'trade_test',
            'sign': 'sign_test'
        }],
        '/json/trade/queryTradeByDate': ["POST", {
            'app_key': 'key_test',
            'date': 'date_test',
            'sign': 'sign_test'
        }],
        '/json/refund/queryRefund': ["POST", {
            'app_key': 'key_test',
            'refund_no': 'refund_test',
            'sign': 'sign_test'
        }],
        '/json/refund/queryRefundByDate': ["POST", {
            'app_key': 'key_test',
            'date': 'date_test',
            'sign': 'sign_test'
        }],
        '/json/refund/doRefund': ["POST", {
            'app_key': 'key_test',
            'out_refund_no': 'out_refund_test',
            'trade_no': 'trade_test',
            'refund_fee': 123456,
            'reason': 'reason_test',
            'notify_url': 'url_test',
            'sign': 'sign_test'
        }],
        '/json/transfer/createWeixinPubTransfer': ["POST", {
            'app_key': 'key_test',
            'type': 'type_test',
            'transfer_fee': 123456,
            'out_transfer_no': 'transfer_test',
            'desc': 'desc_test',
            'openid': 'openid_test',
            'check_name': 'name_test',
            'user_name': 'user_name_test',
            'sign': 'sign_test'
        }]
    },
    'push': {
        '/api/push.json': ["POST", {
            'client_id': '123456',
            'alias': '123456'
        }],
        '/api/alias/get_alias.json': ["POST", {
            'client_id': '123456'
        }],
        '/api/alias/get_clients.json': ["POST", {
            'alias': 'alias'
        }],
        '/api/alias/unbind.json': ["POST", {
            'client': '123456'
        }],
        '/api/tag/add_tag.json': ["POST", {
            'client_id': '123456',
            'tags': 'tags_test'
        }],
        '/api/tag/get_tag.json': ["POST", {
            'client_id': '123456'
        }],
        '/api/tag/remove_tag.json': ["POST", {
            'client_id': '123456',
            'tags': 'tags_test'
        }],
        '/api/task/get.json': ["POST", {
            'task_id': '123456'
        }]
    },
    'shop': {
        '/json/store/get_cate': ["POST", {
            'store_id': 123456,
            'fields': 'fields_test'
        }],
        '/json/store/get_store': ["POST", {
            'appkey': 123456,
            'channel': 'channel_test'
        }],
        '/json/item/get_id': ["POST", {
            'cate_ids': ['1', '2', '3']
        }],
        '/json/item/get_item': ["POST", {
            'item_ids': ['1', '2', '3']
        }],
        '?action=shop_info.html': ["GET", {
            'appkey': 'appkey_test',
            'channel': 'channel_test',
            'id': 123456
        }],
        '?action=login_admin.html': ["GET", {
            'appkey': 'appkey_test',
            'channel': 'channel_test'
        }]
    },
    'splash': {
        '/json/splash/getNewestSplash': ["GET", {
            'app_key': 'key_test',
            'platform': 'IOS'
        }]
    },
    'ucenter': {
        '?action=user_exp_rule.html': ["GET", {
        }],
        '?action=user_jifen_rule.html': ["GET", {
        }],
        '?action=user_config.html': ["GET", {
            'appkey': 'appkey_test',
            'redirect': 'redirect_test'
        }],
        '/json/rpc/third_app_user': ["POST", {
            'appkey': 'appkey_test',
            'token': 'token_test',
            'openid': 'openid_test',
            'nickname': 'name_test',
            'avatar': 'avatar_test'
        }],
        '/json/user_info/register_user': ["POST", {
            'appkey': 'appkey_test',
            'token': 'token_test'
        }],
        '/json/rpc/rpcfetch_user': ["POST", {
            'appkey': 'appkey_test',
            'token': 'token_test'
        }],
        '/json/user_info/get_user_info': ["POST", {
            'appkey': 'appkey_test',
            'token': 'token_test'
        }],
        '/json/rpc/rpcupdate_user': ["POST", {
            'appken': 'appkey_test',
            'token': 'token_test'
        }],
        '/json/user_info/update_user_info': ["POST", {
            'appkey': 'appkey_test',
            'token': 'token_test'
        }],
        '/json/user_address/get_all_addres': ["POST", {
            'appkey': 'appkey_test',
            'token': 'token_test'
        }],
        '/json/user_address/add_address': ["POST", {
            'appkey': 'appkey_test',
            'token': 'token_test',
            'name': 'name_test',
            'phone': '13900000000',
            'county_code': 'code_test',
            'address': 'address_test'
        }],
        '/json/user_address/update_address': ["POST", {
            'address_id': 123456,
            'appkey': 'appkey_test',
            'token': 'token_test',
            'name': 'name_test',
            'phone': '13900000000',
            'county_code': 'county_test',
            'address': 'address_test'
        }],
        '/json/user_address/delete_address': ["POST", {
            'appkey': 'appkey_test',
            'token': 'token_test',
            'address_id': 123456
        }],
        '/json/user_address/update_default_address': ["POST", {
            'appkey': 'appkey_test',
            'token': 'token_test',
            'address_id': 123456
        }]
    },
    'utemplate': {
        '?action=index.html&appkey=$appkey&channel=$channel&id=$id': ["GET", {
            'appkey': 'appkey_test',
            'channel': 123456
        }],
        #'?action=tpl_view.html&appkey=$appkey&channel=$channel&id=$id': ["GET", {
        #    'appkey': 'appkey_test',
        #    'channel': 123456,
        #    'id': 123456
        #}],
        '?action=open.html&appkey=$appkey&rediredt=$url': ["GET", {
            'appkey': 'appkey_test',
            'redirect': 'redirect_test'
        }]
    },
    #'word': {
    #    '/json/type/edit': ["POST", {
    #        'appkey': 'appkey_test',
    #        'channel': 'channel_test',
    #        'type': 'type_test',
    #        'description': 'desc_test'
    #    }],
    #    '/json/word/edit': ["POST", {
    #        'appkey': 'appkey_test',
    #        'channel': 123456,
    #        'type': 'type_test',
    #        'unique_id': 123456,
    #        'word': 'word_test'
    #    }],
    #    '/json/word/delete': ["POST", {
    #        'appkey': 'appkey_test',
    #        'channel': 123456,
    #        'type': 'type_test',
    #        'id': 123456
    #    }],
    #    '/json/word/import': ["POST", {
    #        'appkey': 'appkey_test',
    #        'channel': 123456,
    #        'type': 'type_test',
    #        'file': 'file_test'
    #    }],
    #    '/json/word/hit': ["POST", {
    #        'appkey': 'appkey_test',
    #        'channel': 123456,
    #        'type': 'type_test',
    #        'word_id': 123456
    #    }],
    #    '/json/word/search': ["POST", {
    #        'appkey': 'appkey_test',
    #        'channel': 123456,
    #        'type': 'type_test',
    #        'value': 'value_test'
    #    }],
    #    '/word/main.php?action=index.html': ["POST", {
    #        'appkey': 'appkey_test',
    #        'channel': 123456
    #    }],
    #    '/word/main.php?action=type.html': ["POST", {
    #        'appkey': 'appkey_test',
    #        'channel': 123456,
    #        'type': 'type_test'
    #    }]
    #},
    'agent': {
        '/json/agent_app/all': ["POST", {
            'appkey': 'appkey_test',
            'page': 123456,
            'limit': 123456
        }],
        '/json/agent_app/add': ["POST", {
            'appkey': 'appkey_test',
            'client_appkey': 'client_appkey_test',
            'client_appsecret': 'client_appsecret_test'
        }],
        '/json/agent_app/del': ["POST", {
            'appkey': 'appkey_test',
            'client_appkey': 'client_appkey_test'
        }],
        '/json/agent/all': ["POST", {
            'appkey': 'appkey_test',
            'token': 'appkey_test',
            'page': 123456,
            'limit': 123456
        }],
        '/json/agent/get': ["POST", {
            'appkey': 'appkey_test',
            'agent_id': 123456,
            'token': 'token_test'
        }],
        '/json/agent/add': ["POST", {
            'appkey': 'appkey_test',
            'token': 'token_test',
            'name': 'name_test',
            'owner': 'owner_test',
            'phone': 'phone_test',
            'password': 'password_test',
            'client_appkeys': 'client_appkeys_test'
        }],
        '/json/agent/ban': ["POST", {
            'appkey': 'appkey_test',
            'token': 'token_test',
            'agent_id': 123456
        }],
        '/json/agent/edit': ["POST", {
            'appkey': 'appkey_test',
            'token': 'token_test',
            'agent_id': 123456
        }],
        '/json/agent/all': ["POST", {
            'appkey': 'appkey_test',
            'token': 'token_test',
            'agent_id': 123456,
            'page': 123456,
            'limit': 123456
        }],
        '/json/agent/get': ["POST", {
            'appkey': 'appkey_test',
            'token': 'token_test',
            'client_id': 123456
        }],
        '/json/client/add': ["POST", {
            'appkey': 'appkey_test',
            'token': 'token_test',
            'agent_id': 123456,
            'name': 'name_test',
            'owner': 'owner_test',
            'phone': 13900000000,
            'password': 'password_test',
            'client_appkey': 'client_appkey_test'
        }],
        '/json/client/ban': ["POST", {
            'appkey': 'appkey_test',
            'token': 'token_test',
            'client_id': 123456
        }],
        '/json/client/edit': ["POST", {
            'appkey': 'appkey_test',
            'token': 'token_test',
            'client_id': 123456
        }],
        '/json/item/list': ["POST", {
            'appkey': 'appkey_test'
        }],
        '/json/item/get': ["POST", {
            'appkey': 'appkey_test',
            'item_id': 123456
        }],
        '/json/item/add': ["POST", {
            'appkey': 'appkey_test',
            'name': 'name_test',
            'desc': 'desc_test'
        }],
        '/json/item/del': ["POST", {
            'appkey': 'appkey_test',
             'item_id': 123456
        }],
        '/json/item/edit': ["POST", {
            'appkey': 'appkey_test',
            'item_id': 123456
        }],
        '/json/item/storage_add': ["POST", {
            'appkey': 'appkey_test',
            'item_id': 123456,
            'item_keys': 'keys_test'
        }],
        '/json/item/storage_app_list': ["POST", {
            'appkey': 'appkey_test'
        }],
        '/json/item/storage_agent_list': ["POST", {
            'appkey': 'appkey_test',
            'agent_id': 123456
        }],
        '/json/item/app2agent': ["POST", {
            'appkey': 'appkey_test',
            'agent_id': 'agent_id_test',
            'item_id': 123456,
            'num': 123456
        }],
        '/json/item/agent2client': ["POST", {
            'appkey': 'appkey_test',
            'agent_id': 123456,
            'client_id': 123456,
            'item_id': 123456,
            'num': 123456
        }]
   }
}

# 根据post请求，测试接口，每个接口post2次，0|1用于区分是HTTPError还是URLError
def post_data(url, data, face):
    global error_count
    try:
        # data = data.encode('utf8')
        req = urllib2.Request(url, data)
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')
        req.add_header('Accept', 'application/json')
        response = urllib2.urlopen(req, timeout=8)
        return response.getcode()
    except urllib2.HTTPError as e:
        error_count += 1
        return 0, e.code, e.read()
    except urllib2.URLError as e:
        error_count += 1
        return 1, None, e.reason


# 根据get请求，测试接口
def get_data(url, face):
    global error_count
    try:
        req = urllib2.Request(url)
        req.add_header('Accept', 'application/html')
        response = urllib2.urlopen(req, timeout=8)
        return response.getcode()
    except urllib2.HTTPError as e:
        error_count += 1
        return 0, e.code, e.read()
    except urllib2.URLError as e:
        error_count += 1
        return 1, None, e.reason()


# call_shell主要是写入文件，供call_mail调用
def call_shell(face_name, url, code, exception):
    if not os.path.exists(os.getcwd() + '/interface_txt'):
        os.makedirs(os.getcwd() + '/interface_txt')

    rndtxt = 'interface_txt/' + str(random.randint(10000000, 99999999)) + '.txt'
    if code == None:
        code = "none"

    txt_file = open(rndtxt, 'w+')
    try:
        txt_file.write('接口名: ' + str(face_name) + '\n')
        txt_file.write('url: ' + str(url) + '\n')
        txt_file.write('返回code: ' + str(code) + '\n')
        txt_file.write('exception: ' + str(exception) )
    except:
        txt_file.close()

    txt_file.close()

    # 读取文件内容，存入content，作为邮件发送的内容
    file_obj = open(rndtxt)
    try:
        content = file_obj.read()
    finally:
        file_obj.close()

    call_mail(face_name, rndtxt, content)


# 读取文件内容，调用python自带的邮件发送方法
def call_mail(face_name, rndtxt, content):
    txt_file = open('receivers.txt', 'r')

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
    userpwd = 'Victorpolly123@'
    smtphost = 'smtp.exmail.qq.com'
    smtpport = 465  
         
    #msg = MIMEText(open(rndtxt, 'rb').read(), 'base64', 'utf-8')
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = Header('chenwei90@corp-ci.com', 'utf-8')
    msg['To'] = Header(receivers, 'utf-8')
    
    subject = face_name
    msg['subject'] = Header(subject, 'utf-8')
    try:
        smtpobj = smtplib.SMTP_SSL(smtphost, smtpport)
        smtpobj.login(username, userpwd)
        #for st in receivers_list:
        #接口测试，发邮件
        smtpobj.sendmail(username, receivers_list, msg.as_string())
        smtpobj.quit()
        print u'send succ'
    except smtplib.SMTPException:
        print u'Error: send mail failed'


# 从文件中获取前缀
def getprefixurl():
    global prefixurl
    txt_obj = open('prefixurl.txt', 'r')
    while True:
        line = txt_obj.readline()
        if line:
            prefixurl.append(line.strip())
        else:
            break
    txt_obj.close()


#检测服务器是否能ping通
def monitorServer():
    # urltemp是从prefixurl列表中，截取 xxx.xxx.com部分（去掉前面的协议）
    # 最终形如: ['idg-preprod.tunnel.nibaguai.com', 'oneitfarm.com', 'test.oneitfarm.com']
    urltemp = []
    for k in prefixurl:
        templist = k.split('//')
        temp = templist[1].rstrip('/')
        urltemp.append(temp)

    '''
        1.ping各个前缀, 如果某个没过, 发邮件
        2.如果这个前缀过了, 测试它下面的各个服务, 怎么测? 把它下面所有的接口测一遍
    '''
    for k in urltemp:
        ret = subprocess.call('ping -c 5 ' + k, shell=True, stderr=subprocess.STDOUT)
        if ret == 0:
            # print u'服务器%s ping ok' % k
            i = urltemp.index(k)
            '''
             i是是索引, 0、1、2
             prefixurl[i]对应的是
             http://idg-preprod.tunnel.nibaguai.com/
             https://oneitfarm.com/
             http://test.oneitfarm.com/
            '''
            monitorCurServer(prefixurl[i])
        else:
            # print u'服务器%s ping fail' % k
            # 通知xxx，发邮件
            title = k + ' 域名ping不通'
            content = 'ping了5次，包丢失'
            call_mail(title, '', content)


'''
    1.通用方法
    几个重要变量:
    prefixdict:
        1.这是一个字典
        2.key是服务名, value也是服务名
    reqdict:
        1.这是一个字典
        2.key是服务名, value是一个字典(key1是接口名, value1是列表(0区分post和get, 1是请求参数))
'''
def monitorCurServer(server_url, server_name):
    error_url = []
    #print server_name, server_url, len(reqdict[server_name])
    for k in reqdict[server_name].items():
        #print server_url + '/main.php' + k
        if k[1][0].upper() == 'POST':
            requrl = server_url + '/main.php' + k[0]
            jdata = json.dumps(k[1][1])
            code = post_data(requrl, jdata, k[0])
            if code >= 200 and code <= 206:
                pass
            else:
                code2 = post_data(requrl, jdata, k[0])
                if code2 >= 200 and code2 <= 206:
                    pass
                else:
                    error_url.append(requrl)
                    print u">>>>>>>POST requrl", requrl, "response_code = ", code
        elif k[1][0].upper() == 'GET':
            #print k[0][0]
            if k[0][0] != '?':
                requrl = server_url + '/main.php' + k[0] + '?' + urllib.urlencode(k[1][1])
            else:
                requrl = server_url + '/main.php' + k[0] + '&' + urllib.urlencode(k[1][1])

            code = get_data(requrl, k[0])
            if code >= 200 and code <= 206:
                pass
            else:
                code2 = get_data(requrl, k[0])
                if code2 >= 200 and code2 <= 206:
                    pass
                else:
                    error_url.append(requrl)
                    print u">>>>>>>GET requrl", requrl, "response_code = ", code

    # count表示当前server中, 测试正确的接口数量
    # print "@@@@@@@@@@@@@@@@@@@@@@", server_name, len(error_url)
    if len(error_url) <= 0:
        pass
        #print u">>>>>>>>>>all ok"
    elif len(error_url) == len(reqdict[server_name]):
        call_mail(server_name+'服务', '', server_name + '下面所有的接口测试了两次, 全都不通, 请检查')
    else:
        #pass
        #print u">>>>>>>>>>针对不同的接口,发邮件"
        for k in error_url:
            call_shell(k, requrl, str(code2[1]), code2[2])


def monitorAllServer():
    for k in prefixdict.keys():
        allserver.append(k)

    for k in allserver:
        #print k
        server_url = prefixurl[cur_prefix_idx] + k
        # 测试这个server
        monitorCurServer(server_url, k)


def main():
    getprefixurl()
    monitorAllServer()
    print u'@@@@@@@@@@@@ error_count = ' , error_count


if __name__ == '__main__':
    main()
