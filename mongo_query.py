import pymongo
import timeit
from pymongo import MongoClient
client = MongoClient()
db = client['ikdd_hw15']
collection = db['hw15']

tStart = timeit.default_timer()

db.collection.find({"Uid":"003","Date":"2008-11-19"}).sort([("Time",1)])

tStop = timeit.default_timer()
print "Mongo Query Time =",(tStop-tStart),"s"
