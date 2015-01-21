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
num = 0
def psql_insert(num):
	path = 'Data/00'+str(num)+'/Trajectory/'
	for name in os.listdir(path):
		name_path = os.path.join(path,name)
		i=0
		if os.path.isfile(name_path):
			with open(name_path,'r') as my_file:
				for line in my_file:
					if(i==6):
						query = "INSERT INTO mytb(id,date,time,latitude,longitude) VALUES(%s,%s,%s,%s,%s);"
						data=("00"+str(num),line.split(",")[5],line.split(",")[6].strip("\r\n"),line.split(",")[0],line.split(",")[1])
						mark.execute(query,data)
						connection.commit()
					else:
						i=i+1

if __name__ == "__main__":
	threads = []
	tStart = timeit.default_timer()
	
	t0=threading.Thread(target=psql_insert(0))
	t0.start()
	threads.append(t0)
	t1=threading.Thread(target=psql_insert(1))
	t1.start()
	threads.append(t1)
	t2=threading.Thread(target=psql_insert(2))
	t2.start()
	threads.append(t2)
	t3=threading.Thread(target=psql_insert(3))
	t3.start()
	threads.append(t3)
	t4=threading.Thread(target=psql_insert(4))
	t4.start()
	threads.append(t4)
	t5=threading.Thread(target=psql_insert(5))
	t5.start()
	threads.append(t5)
	for thread in threads:
		thread.join()

	tStop = timeit.default_timer()
	print "Psql Insert Time =",(tStop-tStart),"s"



