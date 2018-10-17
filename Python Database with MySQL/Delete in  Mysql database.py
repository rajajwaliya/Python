import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",passwd="",database="testdb")
cus=con.cursor()

q1="delete from test where name=%s"
q2=("raj",)
cus.execute(q1,q2)
cus.execute("select * from test")
data=cus.fetchall()
for i in data:
    print(i)
print("----------------------")
q1="DROP TABLE IF EXISTS test"
cus.execute(q1)
print("drop table successfully")

con.commit()
cus.close()
con.close()
