from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db=client.xx
collection=db.test
collection.insert({"name":"xx",
                   "age":"23"})
