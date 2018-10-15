import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Test"]
mycol = mydb["Test-Db"]

# insert data for delete
mycol.insert_one({"_id": 9, "name": "manan", "city": "Surat"})

query = {"city": "Surat"}
d = mycol.delete_one(query)

for x in mycol.find():
    print(x)

print("------------------")
mycol.insert_one({"_id": 11, "name": "Ally", "city": "Ahemdabad"})
mycol.insert_one({"_id": 12, "name": "Jolly", "city": "Ahemdabad"})

myqeyry={"city":{"$regex": "^A"}}

delete = mycol.delete_many(myqeyry)

print(delete.deleted_count,"documents are deleted")

#delte all
print("------------------")
delete = mycol.delete_many({})
print(delete.deleted_count,"documents deleted")