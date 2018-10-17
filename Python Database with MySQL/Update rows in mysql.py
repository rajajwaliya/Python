import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", passwd="", database="testdb",buffered=True)
cus = con.cursor()

cus.execute("UPDATE test SET name='def' WHERE name='Amy'")
con.commit()
cus.execute("select * from test limit 5 offset 2")

data = cus.fetchall()
for i in data:
    print(i)

cus.close()
con.close()