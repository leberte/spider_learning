#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Iptest import iptest
import threading
import csv

lock = threading.Lock()

def ipfilter():
    reader = csv.reader(open('ips.csv', 'r'))
    threads = []
    for item in reader:
        it = item[0] + ':' + item[1]
        thread = threading.Thread(target=ipreserve,args=[it])
        threads.append(thread)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


def ipreserve(it):
    lock.acquire()
    IPpool = []
    if iptest(it) == 1:
        IPpool.append(it)
        with open('result_ip.csv','a',newline='') as r:
            csv.writer(r).writerow(IPpool)
    else:
        print('IP%s已被过滤！'%it)
        pass
    lock.release()