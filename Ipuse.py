#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv

def ipuse():
    with open('result_ip.csv', 'r') as r:
        items_1 = csv.reader(r)
        items = [low[0] for low in items_1]
    return items