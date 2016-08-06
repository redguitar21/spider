# -*- coding:utf-8 -*-
# https://www.douban.com/doumail/

import cookielib
import urllib
import urllib2
import sys, time, os, re

filename = 'cookie.txt'
urlmail = 'https://www.douban.com/doumail/'
urllogin = 'https://www.douban.com/accounts/login'

headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
           'Referer': 'http://www.douban.com'}

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

params = {
"form_email":"742218197@qq.com",
"form_password":"rainman1234",
"source":"index_nav" #没有的话登录不成功
}

data = urllib.urlencode(params)

try:
    response = opener.open(urllogin, data)
except urllib2.HTTPError, e:
    print e.code
    print e.reason
except urllib2.URLError, e:
    print e.reason

#print response.read()
#print response.geturl()

# 进入这个分支说明没有登录成功
if response.geturl() == "https://www.douban.com/accounts/login":
    html = response.read()

    # 验证码图片地址
    imgurl = re.search('<img id="captcha_image" src="(.+?)" alt="captcha" class="captcha_image"/>', html)
    if imgurl:
        url = imgurl.group(1)
        # 将图片保存至同目录下
        res = urllib.urlretrieve(url, 'v.jpg')
        # 获取captcha-id参数
        captcha = re.search('<input type="hidden" name="captcha-id" value="(.+?)"/>', html)
        if captcha:
            vcode = raw_input('请输入图片上的验证码：')
            params["captcha-solution"] = vcode
            params["captcha-id"] = captcha.group(1)
            params["user_login"] = "登录"
            # 提交验证码验证
            response = opener.open(urllogin, urllib.urlencode(params))
            #登录成功跳转至首页
            if response.geturl() == "https://www.douban.com/":
                print 'login success ! '
            else:
                print '登陆还是没成功'
                print response.geturl()
                exit(1)

res=opener.open(urlmail)
print res.read()
