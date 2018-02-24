#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Ipspider import ipspider
from Ip_filter import ipfilter

def ipchange(numpage):
    print('ip池重建')
    ipspider(numpage)
    with open('result_ip.csv', 'w') as p:
        p.truncate()
    ipfilter()