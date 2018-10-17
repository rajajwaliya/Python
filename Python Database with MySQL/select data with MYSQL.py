import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", passwd="", database="testdb",buffered=True)
cus = con.cursor()

cus.execute("select * from test")
data = cus.fetchall()

for i in data:
    print("id is :-", i[0], ",name is :-", i[1], ",city is :-", i[2])

print("-----------------")
# print selected value

cus.execute("select name,city from test")
data = cus.fetchall()

for i in data:
    print(i)

print("-----------------")
# print one statment

cus.execute("select * from test")
data = cus.fetchone()

print(data)

print("-----------------")
#condition where
cus.execute("select * from test where name='raj'")
data=cus.fetchall()
for i in data:
    print(i)


con.close()
