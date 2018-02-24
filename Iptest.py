#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import urllib.request

def iptest(ip):
    socket.setdefaulttimeout(4)
    proxy = ip
    proxy_handler = urllib.request.ProxyHandler({"http": proxy})
    opener = urllib.request.build_opener(proxy_handler)
    urllib.request.install_opener(opener)
    try:
        html = urllib.request.urlopen('http://www.baidu.com')
        i = 1
    except Exception :
        print('ip%s无效!'%ip)
        i = 0
    return i