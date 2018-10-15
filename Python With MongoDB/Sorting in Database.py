import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["Test"]

mycol = mydb["Test-Db"]

mydata = mycol.find({}, {"_id": 0}).sort("city", 1)
# 1 for ascending and -1 for descending

for i in mydata:
    print(i)
