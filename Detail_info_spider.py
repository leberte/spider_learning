#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from Iptest import iptest
from Ipuse import ipuse
import socket
from Ipchange import ipchange

header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                     '(KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'}


def my_strip(s):
    return str(s).replace(" ", "").replace("\n", "").replace("\t", "").strip()

def my_Beautifulsoup(request):
    return BeautifulSoup(str(request), 'html.parser')

def detail_info_spider():
    socket.setdefaulttimeout(10)
    file = open('fangyuanlianjie.csv', 'r')
    reader = csv.reader(file)
    file2 = open('information.csv', 'a', newline='')
    writer = csv.writer(file2)
    writer.writerow(['标题', '单价', '小区名字', '地址', '年份', '住宅类型', '大小'
                        , '面积', '朝向', '楼层', '装修类型', '单价', '首付', '网址'])
    m = 0
    global x
    x = ipuse()
    proxy = x[0][0]
    items = [low[0] for low in reader]
    file.close()
    for item in items:
        temp = []
        url = item
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
            request = urllib.request.Request(url, headers=header)
            html = urlopen(request,timeout=10).read()
        except Exception:
            print('爬取第%s项时间过长！'%(items.index(item)+1))
            m += 1
            continue
        soup = BeautifulSoup(html, 'html.parser')
        try:
            result_title = soup.find_all('h3', {'class': 'long-title'})[0]
            result_price = soup.find_all('span', {'class': 'light info-tag'})[0]
            result_house_1 = soup.find_all('div', {'class': 'first-col detail-col'})
            result_house_2 = soup.find_all('div', {'class': 'second-col detail-col'})
            result_house_3 = soup.find_all('div', {'class': 'third-col detail-col'})
            soup_1 = my_Beautifulsoup(result_house_1)
            soup_2 = my_Beautifulsoup(result_house_2)
            soup_3 = my_Beautifulsoup(result_house_3)
            result_house_tar_1 = soup_1.find_all('dd')
            result_house_tar_2 = soup_2.find_all('dd')
            result_house_tar_3 = soup_3.find_all('dd')
            title = my_strip(result_title.text)
            price = my_strip(result_price.text)
            address = my_strip(result_house_tar_1[0].text)
            address2 = my_strip(my_Beautifulsoup(result_house_tar_1[1]).find_all('p')[0].text)
            build_year = my_strip(result_house_tar_1[2].text)
            building_item = my_strip(result_house_tar_1[3].text)
            building_daxiao = my_strip(result_house_tar_2[0].text)
            building_mianji = my_strip(result_house_tar_2[1].text)
            building_chaoxiang = my_strip(result_house_tar_2[2].text)
            buliding_floors = my_strip(result_house_tar_2[3].text)
            building_leixing = my_strip(result_house_tar_3[0].text)
            building_danjia = my_strip(result_house_tar_3[1].text).encode('utf-8').rstrip(b'\xe5\x85\x83/m\xc2\xb2').decode('gbk')
            building_shoufu = my_strip(result_house_tar_3[2].text)
            temp.append(title)
            temp.append(price)
            temp.append(address)
            temp.append(address2)
            temp.append(build_year)
            temp.append(building_item)
            temp.append(building_daxiao)
            temp.append(building_mianji)
            temp.append(building_chaoxiang)
            temp.append(buliding_floors)
            temp.append(building_leixing)
            temp.append(building_danjia)
            temp.append(building_shoufu)
            temp.append(url)
            writer.writerow(temp)
            print('第%s页打印完毕'%(items.index(item)+1))
        except IndexError :
            print('ip被封！更换IP')
            print('ip%s将被删除' % x[m])
            x.remove(x[m])
            if (m + 1) > len(x):
                ipchange(1)
                m = 0
                x = ipuse()
            continue
    file2.close()
