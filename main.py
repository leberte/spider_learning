#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Ipspider import ipspider
from Ip_filter import ipfilter
from Detail_info_spider import detail_info_spider
from URL_spider import URLspider



def main():
    ipspider(1)
    print('ip爬取完毕！')
    ipfilter()
    print('ip筛选完毕！')
    URLspider()
    detail_info_spider()
    print('DONE!')



if __name__ == '__main__':
    main()