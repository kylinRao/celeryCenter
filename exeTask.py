#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 23:36
# @Author  : Aries
# @Site    : 
# @File    : exeTask.py
# @Software: PyCharm
from tasks import execute
sqltemp = "replace into test VALUES ({id},'name{id}','des');"
for id in xrange(100000,2000000):
    execute(sqltemp.format(id=id))