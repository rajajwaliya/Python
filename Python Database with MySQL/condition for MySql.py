import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", passwd="", database="testdb")
cus = con.cursor()

cus.execute("select * from test where city='def'")
data = cus.fetchall()
for i in data:
    print(i)
print("------------------------")
inp = input("enter name you want to search :- ")
q1 = "select * from test where name=%s"
q2 = (inp,)
cus.execute(q1, q2)
data = cus.fetchall()
for i in data:
    print(i)
print("------------------------")
print("names like r")
q1 = "select * from test where name like '%r%'"
cus.execute(q1)
data = cus.fetchall()
for i in data:
    print(i)
