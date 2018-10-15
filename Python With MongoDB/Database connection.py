import pymongo

#if you  dont enter data in collection
#then database and collection are not created

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["Test"]

mycol = mydb["Test-Db"]

mydata = {"name":"raj","city":"bhavnagar"}

x=mycol.insert_one(mydata)

mydblist = myclient.list_database_names()

print(mydblist)

print(mydb.list_collection_names())

if "Test-Db" in mydb.list_collection_names():
    print("database connect successfully")

print(x)