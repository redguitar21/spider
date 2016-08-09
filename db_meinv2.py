# -*- coding:utf-8 -*-
# http://tieba.baidu.com/p/4713369340

# rsg 这个版本用二进制下载, 希望能稳定很多

import cookielib
import urllib
import urllib2
import sys, time, os, re
from bs4 import BeautifulSoup
import requests

url_target = 'http://www.dbmeinv.com'
#urllogin = 'https://www.douban.com/accounts/login'

headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
           'Referer': 'http://www.douban.com'}

#url_target = raw_input('请输入贴吧地址:').strip()
print '正在开启下载...'

#html = urllib2.urlopen(url_target)
#print html.read()

html = requests.get(url_target, headers=headers).content

soup = BeautifulSoup(html,"html.parser")


#item = soup.find('div', class_ = "sender")

#print item



j = 0
# 挨个获取来信列表
for item in soup.find_all('img', class_ = "height_min"):
    print item
    #print '\n'

    #print item.a.string
    j += 1
    print '\n-----------------------------'

print (u'页面共有%s个美女' %j)

title = soup.find('title').string

if(os.path.exists(title) == False):
    os.mkdir(title)



count = 1
yeshu = 1
imgfailed = []

while(1):

    imglist = soup.find_all('img', class_ = "height_min")
    #print imglist


    x = 1
    for i in imglist:
        name = i.get('alt')
        #name_a = name.encode("utf-8")
        #name.replace('/', '_')
        #print repr(name)

        imgurl = i.get('src')
        image = urllib.urlopen(imgurl).read()

        pathname = './%s/%s_%s.jpg' % (title, count, name)

        try:
            with open(pathname, "wb") as pic:
                pic.write(image)
                pic.close()
            #urllib.urlretrieve(imgurl, './%s/%s_%s.jpg' % (title, count, name))
        except IOError:
            imgfailed.append(imgurl)
            print '图片下载失败, 跳过...'
            continue

        print (u'下载%s页第 %s 张' %(yeshu, x))
        x += 1
        count += 1

    nextye = soup.find('a', title="下一页")
    if(nextye):
        nexturl = nextye.get('href')
        url_target = 'http://www.dbmeinv.com' + nexturl
    else:
        print '\n下载完毕! \n'
        break

    print url_target
    yeshu += 1
    print ('准备下载第%s页....\n\n\n', yeshu)

    # 读取新的页面
    html = requests.get(url_target, headers=headers).content
    soup = BeautifulSoup(html, "html.parser")

if(str(len(imgfailed)) > 0):
    print '共下载图片 ' + str(count) + ' 张, 其中失败 ' + str(len(imgfailed))+ ' 张, 如下:'
    print '---------------------------\n'
    for m in imgfailed:
        print m
        print '\n'

    print '---------------------------\n'
    print '请手动下载'

else:
    print '共下载图片 ' + str(count) + ' 张, 全部下载成功'