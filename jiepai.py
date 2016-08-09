# -*- coding:utf-8 -*-


import cookielib
import urllib
import urllib2
import sys, time, os, re

#
# http://www.jpscds.com/plus/read2.php

url_target = 'http://www.jpscds.com/plus/read2.php'

headers = {
    "Host": "passport.baidu.com",
    "Referer": "http://www.baidu.com/cache/user/html/login-1.2.html",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
    "Origin": "http://www.baidu.com",
    """yufang xiao tou.  this code by zhengxiao(www.zh30.om)"""
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive"
}



params = {
    "ac":":buycount",
}

data = urllib.urlencode(params)

try:
    #response = urllib2.Request(url_target, headers=headers, data=data)
    response = urllib2.urlopen(url_target, data)
    print response.read()

except urllib2.HTTPError, e:
    print e.code
    print e.reason
except urllib2.URLError, e:
    print e.reason
