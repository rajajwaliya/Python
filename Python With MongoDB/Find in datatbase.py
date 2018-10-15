import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["Test"]

mycol = mydb["Test-Db"]

for i in mycol.find():
    print(i)

#Return Only Some Fields

print()
for n in mycol.find({},{"_id":0,"name":1,"city":1}):
    print(n)