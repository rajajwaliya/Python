import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Test"]
mycol = mydb["Test-Db"]

mydata = mycol.find().limit(10)

for i in mydata:
    print(i)