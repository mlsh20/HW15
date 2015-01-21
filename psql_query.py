#!/usr/bin/python
# -*- coding: utf-8 -*-
import psycopg2
import os
import sys
import threading,timeit
import thread

conn_str = "dbname='mydb' user='postgres' host='localhost' password='25263238a'"
connection = psycopg2.connect(conn_str)
mark = connection.cursor()

query = "select id,date,time from mytb where id='003' and date='2008-11-19' order by time;"

tStart = timeit.default_timer()
mark.execute(query)
tStop = timeit.default_timer()
print "Psql Query Time = ",(tStop-tStart),"s"
