# -*- coding:utf-8 -*-
# Python 2 code
import urllib
import urllib2
import requests

# RSG注

# 此url为百度的好压软件下载链接, 测试用
url = 'http://sw.bos.baidu.com/sw-search-sp/software/530e3005a55/haozip_baidu_5.8.2.10651_setup.exe'


# 方法一: 用url-retrieve
print "downloading with urllib"
urllib.urlretrieve(url, "code.zip")

print 'finished.'


# 方法二: 用urlopen 后读取的数据, 直接存成文件
print "downloading with urllib2"
f = urllib2.urlopen(url)
data = f.read()
with open("code2.zip", "wb") as code:
    code.write(data)

print 'finished.'


# 方法三: 用requests组件, 打开url后获取content中的内容存到本地文件中
print "downloading with requests"
r = requests.get(url)
with open("code3.zip", "wb") as code:
    code.write(r.content)

print 'finished.'


