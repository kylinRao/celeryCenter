#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 23:36
# @Author  : Aries
# @Site    : 
# @File    : exeTask.py
# @Software: PyCharm
from tasks import execute
sqltemp = "replace into test VALUES (%s,%s,'des');"
metaList = []
count = 0
for id in xrange(1,10000001):
    metaList.append((id,"name"+str(id)))
    if id%100000 == 0:
        count = count +1
        print count
        execute.delay(sqltemp,metaList)
        metaList=[]