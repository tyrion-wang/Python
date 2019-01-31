#-*- coding: UTF-8 -*-

import sys
import urllib
from urllib.parse import quote
import urllib3
import requests
import certifi
import numpy
import time
import json
import myLib.mHeader

def getHttps3(url):
    print(url)
    time.sleep(numpy.random.rand()*5)
    
    header = mHeader.random()
    print(header)
    response = requests.get(url, header) 
    #print(response.text)
    
    for i in response.json()['data']:
        print(i['title'])
        print(i['rate'])
        print(i['url'])

if __name__=='__main__':
    tag = "电影";
    genres = "剧情";
    start = 0 #最大值为9979，之后返回空
    
    #url='https://movie.douban.com/j/search_subjects?type=movie&tag='+tag_gb2312+'&sort=recommend&page_limit=20&page_start=2'
    #url="https://movie.douban.com/j/search_subjects?type=movie&tag=%s&sort=recommend&page_limit=20&page_start=0" % tag.encode('utf-8')
    #url='https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags='+tag_gb2312+'&start=0'
    #url='https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags='+tag_gb2312+'&start=0'
    url='https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags='+quote(tag, 'utf-8')+'&start='+str(start)+'&genres='+quote(genres, 'utf-8')
    getHttps3(url)