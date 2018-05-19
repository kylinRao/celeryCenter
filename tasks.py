#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 23:27
# @Author  : Aries
# @Site    : 
# @File    : tasks.py
# @Software: PyCharm
#tasks.py
import MySQLdb
from celery import Celery

app = Celery('tasks',  backend='redis://192.168.1.112:6379/0', broker='redis://192.168.1.112:6379/0') #配置好celery的backend和broker

@app.task  #普通函数装饰为 celery task
def add(x, y):
    return x + y
@app.task
def execute(sql,metaList):
    conn = MySQLdb.connect("192.168.1.112", "admin", "Huawei123", "adminserver", charset='utf8' )
    cur =conn.cursor()
    cur.executemany(sql,metaList)
    conn.commit()
    conn.close()