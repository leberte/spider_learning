#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import socket


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
                 '(KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'
headers = {'User-agent': user_agent}
socket.setdefaulttimeout(10)


def ipspider1(url1,numpage):
    for num in range(1, numpage + 1):
        ipurl = url1 + str(num)
        print("Now downloading the " + str(num * 100) + ' ips')
        for i in range(Max_Num):
            try:
                request = urllib.request.Request(ipurl, headers=headers)
                content = urlopen(request,timeout=10).read()
                bs = BeautifulSoup(content, 'html.parser')
                res = bs.findAll('tr')
                for item in res:
                    try:
                        temp = []
                        tds = item.findAll('td')
                        temp.append(tds[1].text)
                        temp.append(tds[2].text)
                        writer.writerow(temp)
                    except IndexError:
                        pass
                break
            except :
                if i < Max_Num - 1:
                    continue
                else:
                    print('URLError: <urlopen error timed out> All times is failed , the  URL2 DEAD')
    print('URL1爬取完毕！')


def ipspider2(url2):
    for i in range(Max_Num):
        try:
            request = urllib.request.Request(url2, headers=headers)
            content2 = urlopen(request, timeout=10).read()
            bs2 = BeautifulSoup(content2, 'html.parser')
            res2 = bs2.findAll('ul', {'class': 'l2'})
            for item in res2:
                result_li = item.findAll('li')
                try:
                    temp2 = []
                    temp2.append(result_li[0].text)
                    temp2.append(result_li[1].text)
                    writer.writerow(temp2)
                except IndexError:
                    pass
            break
        except :
            if i < Max_Num - 1:
                continue
            else:
                print('URLError: <urlopen error timed out> All times is failed ,the  URL2 DEAD')
    print('URL2爬取完毕！')




def ipspider(numpage):
    csvfile = open('ips.csv', 'w', newline='')
    global writer
    global Max_Num
    Max_Num = 6
    writer = csv.writer(csvfile)
    url1 = 'http://www.xicidaili.com/nn/'
    url2 = 'http://www.data5u.com/free/gngn/index.shtml'
    ipspider1(url1,numpage)
    ipspider2(url2)
    csvfile.close()
