# -*- coding:utf-8 -*-
# https://www.douban.com/doumail/

import cookielib
import urllib
import urllib2
import sys, time, os, re
from bs4 import BeautifulSoup
import requests

filename = 'cookie_jp.txt'
url_target = 'http://www.jpscds.com/plus/view.php?aid=29843'
urllogin = 'http://www.jpscds.com/member/index.php'

mycookie = {'PHPSESSID': 'ev6rr771oh1r10p13dd2adjt85', 'DedeUserID' : '38115', 'DedeUserID__ckMd5' : '5de46641094deddb', 'DedeLoginTime' : '1470746834',  'DedeLoginTime__ckMd5' : '025644717da71965'}

headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
           'Referer': 'http://www.douban.com'}



# 用浏览器cookies直接登录
#response = requests.get(urllogin, cookies=mycookie)
#print response.text

#print '登陆成功! '



#response = urllib2.urlopen(urllogin)


# 打开目标网页
#response = requests.get(url_target, cookies=mycookie)
#print response.text

params = {
    "ac":"down",
    "aid":"8574"
}

data = urllib.urlencode(params)

url3 = 'http://www.jpscds.com/plus/read.php'
response = requests.get(url3, data, cookies=mycookie)

print response.text