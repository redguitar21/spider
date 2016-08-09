#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests, re, json, html2text, sys, time
from bs4 import BeautifulSoup
import time
import os


baseurl = "http://jandan.net/ooxx/page-"
# 伪装成浏览器去访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
    'Accept-Encoding': 'gzip',
    'Cookie': '1024679722=aada4mZxRMxqvInd7D6PSgq%2FIkpGFeGlZWAH1gqP8Q; __auc=57bffd35154a91de3cd5d3b1ddb; 1024679722=ebeaLZUFikSR1OE6lm5MJYJSV0V1DbcooxQr0CHu; jdna=596e6fb28c1bb47f949e65e1ae03f7f5#1467948344088; Hm_lvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1467001661,1467189261,1467685014,1467857178; Hm_lpvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1467948345; _ga=GA1.2.1739476572.1438849462; _gat=1'}


def getImageList():
    # 想抓页，自己定义
    for x in range(1, 30):
        page = 2006 - x  # 按照网页浏览方式，起始页数，然后递减，这里可以随意修改
        current_url = baseurl + str(page)
        response = url_open(current_url)
        if "check_human" in response.text:
            # 被屏蔽，休息1分钟 ，建议抓取的频率不要太频繁，太频繁一样会被屏蔽
            time.sleep(60)
        else:
            soup = BeautifulSoup(response.text, "html.parser")
            divList = soup.find_all("div", class_='text')
            for i in divList:
                img = i.p.img;
                if len(i.contents) > 1 and img != None:
                    href = img.get("src")
                    saveImage(href)
        time.sleep(3)


def saveImage(imgUrl):
    fileName = imgUrl[imgUrl.rfind("/") + 1:]
    path = r"./jiandanxxoo/" + fileName  # 这里改成你自己的本地目录
    response = url_open(imgUrl)
    image = response.content
    with open(path, "wb") as f:
        f.write(image)
        f.close()


def url_open(url):
    print("get url ### " + url)
    return requests.get(url, headers=headers)


if __name__ == "__main__":
    getImageList()