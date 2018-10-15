import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["Test"]

mycol = mydb["Test-Db"]

# find the specific row data

myquery = {"_id": 5}

x = mycol.find(myquery)

for i in x:
    print(i)

# find data with advanced query
print("--------------------")
myquery1 = {"_id": {"$lt": 4}}


x1 = mycol.find(myquery1)


for i1 in x1:
    print(i1)
print("--------------------")
myquery2 = {"city": {"$gt": "O"}}

y1 = mycol.find(myquery2)

for i2 in y1:
    print(i2)


#With Regular Expressions


print("--------------------")
myquery3 = {"city":{"$regex":"^S"}}
x2=mycol.find(myquery3)
for i3 in x2:
    print(i3)