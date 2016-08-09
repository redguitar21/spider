# coding:utf-8
####################################################
# coding by 刘云飞
####################################################

import requests
import os
import time
import random
from bs4 import BeautifulSoup
import threading

url = "http://jandan.net/ooxx/page-"
img_lists = []
url_lists = []
not_url_lists = []
ips = []
thread_list = []

with open('ip2.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        ip_one = "http://" + line.strip()
        ips.append(ip_one)

headers = {
    'Host': 'jandan.net',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/42.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Referer': 'http://jandan.net/ooxx/',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
}

for i in range(1530, 1883):
    url_lists.append(url + str(i) + '#comments')


def writeToTxt(name, list):
    with open(name, 'w+') as f:
        for urlOne in list:
            f.write(urlOne + "\n")


def get_img_url(url):
    single_ip_addr = random.choice(ips)
    lists_tmp = []
    page = int(url[28:32])
    filename = str(page) + ".txt"
    proxies = {'http': single_ip_addr}
    try:
        res = requests.get(url, headers=headers, proxies=proxies)
        print(res.status_code)
        if res.status_code == 200:
            text = res.text
            Soup = BeautifulSoup(text, 'lxml')
            results = Soup.find_all("a", target="_blank", class_="view_img_link")
            for img in results:
                lists_tmp.append(img['href'])
                url_lists.append(img['href'])
            print(url + "  --->>>>抓取完毕！！")
            writeToTxt(filename, lists_tmp)
        else:
            not_url_lists.append(url)

            print("not ok")
    except:
        not_url_lists.append(url)
        print("not ok")


for url in url_lists:
    page = int(url[28:32])
    filename = str(page) + ".txt"
    if os.path.exists(filename):
        print(url + "   is pass")
    else:
        # time.sleep(1)
        get_img_url(url)

print(img_lists)

with open("img_url.txt", 'w+') as f:
    for url in img_lists:
        f.write(url + "\n")

print("共有 " + str(len(img_lists)) + " 张图片。")
print("all done!!!")

with open("not_url_lists.txt", 'w+') as f:
    for url in not_url_lists:
        f.write(url + "\n")

