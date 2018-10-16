import sqlite3
import time
import datetime
import random

con = sqlite3.connect("Insert.db")
cus = con.cursor()
cus.execute("CREATE TABLE IF NOT EXISTS InsertDb (name TEXT,city TEXT,timestamp TEXT,value INTEGER)")

for i in range(2):
    datatime = str(datetime.datetime.fromtimestamp(time.time()).strftime('%d/%m/%Y %H:%M:%S'))
    name = input("enter your name :- ")
    city = input("enter your city :- ")
    value = int(random.randrange(1000, 9000))
    cus.execute("INSERT INTO InsertDb(name,city,timestamp,value) VALUES (?,?,?,?)",(name, city, datatime, value))
    con.commit()
    print("your data insert successfully")
    print("-------------------")
    time.sleep(1)

cus.close()
con.close()