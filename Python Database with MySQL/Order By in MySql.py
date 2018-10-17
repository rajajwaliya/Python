import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",passwd="",database="testdb")
cus=con.cursor()

cus.execute("SELECT * FROM test ORDER BY name")
data=cus.fetchall()
# print([i for i in data])
for i in data:
    print(i)

print("------------------")
# decrement order
cus.execute("SELECT * FROM test ORDER BY id desc")
data=cus.fetchall()
for i in data:
    print(i)