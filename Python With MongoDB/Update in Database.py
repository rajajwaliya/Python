import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Test"]
mycol = mydb["Test-Db"]

query1 = {"city":"Surat"}
query2 = {"$set" :{"city":"Bhavnagar"}}

myupdate = mycol.update_one(query1,query2)
print(myupdate)

#multiple upddates

query1 = {"name":{"$regex":"^R"}}
query2 = {"$set" :{"name":"Raj"}}

myupdate2= mycol.update_many(query1,query2)

print(myupdate2.modified_count,"are updated")