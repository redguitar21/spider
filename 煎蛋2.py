#/usr/bin/env python3.5
# -*- coding: utf-8 -*-
__author__ = 'zenway33'

from bs4 import BeautifulSoup
import requests
import time
import random
import os

# 建立一个目录用于存储下载的文件:
img_dir = 'jiandanxxoo20160612'
if not os.path.isdir(img_dir):
    os.mkdir(img_dir)

# 获取一个随机的header
def random_header():
    #def LoadUserAgents(uafile="user_agents.txt"):
    def load_useragents(uafile="user_agents.txt"):
            """
            uafile : string
                path to text file of user agents, one per line
            """
            uas = []
            with open(uafile, 'rb') as uaf:
                for ua in uaf.readlines():
                    if ua:
                        uas.append(ua.strip()[1:-1-1])
            random.shuffle(uas)
            return uas

    # load the user agents, in random order
    uas = load_useragents(uafile="user_agents.txt")
    # load user agents and set headers
    ua = random.choice(uas)  # select a random user agent
    headers = {
        "Connection" : "close",  # another way to cover tracks
        "User-Agent" : ua}
    return headers


# proxy = {"http": "http://username:p3ssw0rd@10.10.1.10:3128"}
'''
headers = {
       'User-Agent': 'Mozilla/5.8 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'
}
'''

# 单个页面的内容抓取分析
'''
url = 'http://jandan.net/ooxx/page-2007'
wb_data = requests.get(url,headers=headers)
soup = BeautifulSoup(wb_data.text,'lxml')

imgs = soup.select('p > img')

for img_url in imgs:
    url = img_url.get('src')
    print(url)
'''


# 下载文件,保存本地
def download(image_url, image_name):
    headers = random_header()
    r = requests.get(image_url, stream = True,headers=headers)
    #with open(path + '/' + '{}.jpg'.format(index), "wb") as fs:
    with open(os.path.join(img_dir, image_name), 'wb') as fs:
        fs.write(r.content)
        fs.close
    print("filename: %s , image_url: %s... is download" % (image_name, image_url))

# 获取图片url
def get_image_info():
    for page_num in range(2000,2015):

            headers = {
                       'User-Agent': 'Mozilla/5.8 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                       'Accept-Encoding': 'none',
                       'Accept-Language': 'en-US,en;q=0.8',
                       'Connection': 'keep-alive'
                      }

            wb_data =requests.get('http://jandan.net/ooxx/page-{}'.format(page_num), headers=headers)
            time.sleep(5)
            soup = BeautifulSoup(wb_data.text,'html.parser')
            image_urls =  soup.select('p > img')
            print("page_num: %s" % page_num)

            try:
                for index,image_url in enumerate(image_urls):
                    image_url = image_url.get('src')
                    data = {
                        'image_url' :image_url,
                        #'image_name'  :image_url.split('/')[-1]
                        'image_name' :'{}.jpg'.format(index)

                    }
                    #print(data)
                    image_url = data['image_url']
                    image_name = str(page_num) + '_' + data['image_name']
                    #download images
                    download(image_url, image_name)
            except:
                pass

if __name__ == "__main__":
    start_time = time.time()
    get_image_info()
    print("--- %s seconds ---" % (time.time() - start_time))