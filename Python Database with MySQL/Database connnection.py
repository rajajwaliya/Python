import mysql.connector

# install driver go to settings>project interpreter>search mysql-conector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="")
    #,database="TestDb")
print(con)

cus = con.cursor()
cus.execute("CREATE DATABASE IF NOT EXISTS TestDb")
cus.execute("SHOW DATABASES")
for i in cus:
    print(i)
