# -*- coding:utf-8 -*-
# http://tieba.baidu.com/p/4713369340

# rsg 2016-8-5 查看都有列表 并且列出简略内容, 下载对应头像

import cookielib
import urllib
import urllib2
import sys, time, os, re
from bs4 import BeautifulSoup

filename = 'cookie_db.txt'
url_target = 'http://tieba.baidu.com/p/3991804067'
#urllogin = 'https://www.douban.com/accounts/login'

headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
           'Referer': 'http://www.douban.com'}

url_target = raw_input('请输入贴吧地址:').strip()
print '正在开启下载...'

html = urllib2.urlopen(url_target)
#print html.read()

soup = BeautifulSoup(html.read(),"html.parser")


#item = soup.find('div', class_ = "sender")

#print item



# 挨个获取来信列表
for item in soup.find_all('img', class_ = "BDE_Image"):
    print item
    #print '\n'

    #print item.a.string
    print '\n-----------------------------'

title = soup.find('title').string

if(os.path.exists(title) == False):
    os.mkdir(title)



count = 1
yeshu = 1

while(1):

    imglist = soup.find_all('img', class_ = "BDE_Image")
    #print imglist


    x = 1
    for i in imglist:
        imgurl = i.get('src')
        urllib.urlretrieve(imgurl, './%s/%s %s.jpg' % (title, title, count))
        print (u'下载%s页第 %s 张' %(yeshu, x))
        x += 1
        count += 1

    nextye = soup.find('a', text="下一页")
    if(nextye):
        nexturl = nextye.get('href')
        url_target = 'http://tieba.baidu.com' + nexturl
    else:
        print '\n下载完毕! \n'
        break

    print url_target
    yeshu += 1
    print ('准备下载第%s页....\n\n\n', yeshu)

    # 读取新的页面
    html = urllib2.urlopen(url_target)
    soup = BeautifulSoup(html.read(), "html.parser")


