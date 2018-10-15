import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["Test"]

mycol = mydb["Test-Db"]

mydata = {"name": "manan", "city": "Surat"}

x = mycol.insert_one(mydata)

print(x.inserted_id)

# inser multiple data

mydatamul = [
    {"name": "Amy", "city": "Apple st 652"},
    {"name": "Hannah", "city": "Mountain 21"},
    {"name": "Michael", "city": "Valley 345"},
    {"name": "Sandy", "city": "Ocean blvd 2"},
    {"name": "Betty", "city": "Green Grass 1"}]

y = mycol.insert_many(mydatamul)

print(y.inserted_ids)

datawithid = [
    {"_id": 1, "name": "Susan", "city": "One way 98"},
    {"_id": 2, "name": "Vicky", "city": "Yellow Garden 2"},
    {"_id": 3, "name": "Ben", "city": "Park Lane 38"},
    {"_id": 4, "name": "William", "city": "Central st 954"},
    {"_id": 5, "name": "Chuck", "city": "Main Road 989"},
    {"_id": 6, "name": "Viola", "city": "Sideway 1633"}]

z = mycol.insert_many(datawithid)

print(z.inserted_ids)
