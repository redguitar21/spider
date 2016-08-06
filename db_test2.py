# -*- coding:utf-8 -*-
# https://www.douban.com/doumail/

import cookielib
import urllib
import urllib2
import sys, time, os, re
from bs4 import BeautifulSoup

filename = 'cookie_db.txt'
urlmail = 'https://www.douban.com/doumail/'
urllogin = 'https://www.douban.com/accounts/login'

headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
           'Referer': 'http://www.douban.com'}

#cookie = cookielib.CookieJar()
if(os.path.exists('./cookie_db.txt') == False):
    cookie = cookielib.MozillaCookieJar(filename)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

    # 设置用户名、密码
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

                    # 保存cookie到文件
                    cookie.save(ignore_discard=True, ignore_expires=True)

                else:
                    print '登陆还是没成功'
                    print response.geturl()
                    exit(1)

else:
    # 已经登陆的情况下
    cookie = cookielib.MozillaCookieJar()
    # 从文件中读取cookie内容到变量
    cookie.load('cookie_db.txt', ignore_discard=True, ignore_expires=True)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    print '已有cookies, 直接登陆'


html=opener.open(urlmail)
#print html.read()

soup = BeautifulSoup(html.read(),"html.parser")


#for tag in soup.find_all(True):
#    print(tag.name)


#item = soup.find('div', class_ = "sender")

#print item
print '来信列表:\n'

names = []

# 挨个获取来信列表
for item in soup.find_all('div', class_ = "title"):
    #print item
    #print '\n'
    date = (item.span.string)
    name = item.span.find_next_sibling().string
    print u'日期: ' + date
    print u'来信者: ' + name
    print u'内容: ' + item.a.string
    #print item.a.string
    print '\n-----------------------------'
    names.append(name)


# 下载头像
imglist = soup.find_all('img', src=re.compile('icon'))
print imglist

x = 0
for i in imglist:
    imgurl = i.get('src')
    urllib.urlretrieve(imgurl, '%s.jpg' % names[x])
    print (u'下载 %s 的头像' % names[x])
    x += 1