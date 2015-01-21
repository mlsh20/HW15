import pymongo
import datetime
import os
import sys
import threading,timeit
import time,itertools
from pymongo import MongoClient
client = MongoClient()
db = client['ikdd_hw15']

def mongo_insert(num):
	path = 'Data/00'+str(num)+'/Trajectory/'
	collection_name="hw15_00"+str(num)
	dbcollection = db.collection_name
	#hw15_000 = db.hw15_000
	for name in os.listdir(path):
		name_path = os.path.join(path,name)
		i=0
		if os.path.isfile(name_path):
			with open(name_path,'r') as my_file:
				for line in my_file:
					if(i==6):
						id="00"+str(num)
						data = {"Uid":id,"Date":line.split(",")[5],"Time":line.split(",")[6].strip("\r\n"),"Lat":line.split(",")[0],"Lon":line.split(",")[1]}
						dbcollection.insert(data)
					else:
						i=i+1

if __name__ == "__main__":
	threads = []
	tStart = timeit.default_timer()

	t0=threading.Thread(target=mongo_insert(0))
	t0.start()
	threads.append(t0)
	t1=threading.Thread(target=mongo_insert(1))
	t1.start()
	threads.append(t1)
	t2=threading.Thread(target=mongo_insert(2))
	t2.start()
	threads.append(t2)
	t3=threading.Thread(target=mongo_insert(3))
	t3.start()
	threads.append(t3)
	t4=threading.Thread(target=mongo_insert(4))
	t4.start()
	threads.append(t4)
	t5=threading.Thread(target=mongo_insert(5))
	t5.start()
	threads.append(t5)

	for thread in threads:
		thread.join()
	tStop = timeit.default_timer()
	print "Mongo Insert Time =",(tStop-tStart),"s"
