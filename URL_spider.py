#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from Iptest import iptest
from Ipuse import ipuse
from Ipchange import ipchange

url = 'https://suizhou.anjuke.com/sale/'
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                 '(KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'}


def URLspider():
    m = 0
    i = 1
    global x
    x = ipuse()
    proxy = x[0]
    while(i):
        file = open('fangyuanlianjie.csv', 'a', newline='')
        writer = csv.writer(file)
        result_url = url + 'p'+str(i) + '/'+'#filtersort'
        while (True):
            if iptest(x[m]) == 1:
                proxy = x[m]
                if (m + 1) > len(x):
                    ipchange(1)
                    m = 0
                    x = ipuse()
                break
            else:
                print('ip%s被删除' % x[m])
                x.remove(x[m])
                if (m + 1) > len(x):
                    ipchange(1)
                    m = 0
                    x = ipuse()
        proxy_handler = urllib.request.ProxyHandler({"http": proxy})
        opener = urllib.request.build_opener(proxy_handler)
        urllib.request.install_opener(opener)
        try:
            request = urllib.request.Request(result_url, headers = header)
            html = urlopen(request).read()
            info = BeautifulSoup(html, 'html.parser')
            result_li = info.findAll('li',{'class':'list-item'})
            for li in result_li:
                temp = []
                page_url = str(li)
                info2 = BeautifulSoup(page_url, 'html.parser')
                result_href = info2.findAll('a',{'class':'houseListTitle'})[0]
                temp.append(result_href.attrs['href'])
                writer.writerow(temp)
        except Exception:
            print('第%d页爬取错误，将进入下一页！'%i)
            i += 1
            file.close()
            continue
        print('第%d页爬取成功，将进入下一页！'%i)
        file.close()
        result_next_page = info.findAll('a',{'class':'aNxt'})
        if len(result_next_page) != 0:
            i = i + 1
        else:
            print('总共共包含%d页'%i)
            print('没有下一页了！')
            i = 0