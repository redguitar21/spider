# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import urllib2


url_target = 'http://www.jandan.net/ooxx'
#urllogin = 'https://www.douban.com/accounts/login'

headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
           'Referer': 'http://www.jandan.net/'}

#url_target = raw_input('请输入贴吧地址:').strip()
print '正在开启下载...'

html = urllib2.urlopen(url_target)

soup = BeautifulSoup(html.read(),"html.parser")


print soup

i = 1
for index, each in enumerate(soup.select('#comments img')):
    with open('{}.jpg'.format(index), 'wb') as jpg:
        jpg.write(requests.get(each.attrs['src'], stream=True).content)
        print i
        i += 1