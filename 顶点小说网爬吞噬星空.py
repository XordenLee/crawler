#!/user/bin/env python
# -*- coding: utf-8 -*-
# @Author : XordenLee
# @Time   : 2019/2/1 18:51

from bs4 import BeautifulSoup as sb
import requests
import json

def get_chapter(url, file_obj):
    res = requests.get(url)
    res.encoding = 'gbk'
    soup = sb(res.text, 'lxml')
    chapter_name = soup.select('.bookname h1')[0].text.strip()
    print('Getting '+chapter_name)
    file_obj.write('\n\n' + chapter_name)
    for ss in soup.select('#content')[0]:
        if len(ss) > 0:
            file_obj.write('\n    ' + ss.strip())
    print('Writing down!')

surl = 'https://www.booktxt.net/1_1722/'
file_path = 'E:/python/test/'

req = requests.get(surl)
req.encoding = 'gbk'

soup = sb(req.text,'lxml')
name = soup.select('#info h1')[0].text
author = soup.select('#info')[0].contents[3].text.split('：')[1]
with open(file_path+name+'.txt', 'w') as fi:
    fi.write(name+'\n作者：'+author)
    dls = soup.select('dl')[0]
    for dd in dls.select('dd')[8:]:
        nurl = dd.select('a')[0]['href']
        get_chapter(surl + nurl, fi)
