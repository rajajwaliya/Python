import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", passwd="", database="testdb")
cus = con.cursor()

cus.execute("CREATE TABLE IF NOT EXISTS test (id INT AUTO_INCREMENT PRIMARY KEY,name TEXT)")
cus.execute("SHOW TABLES")
for i in cus:
    print(i)

cus.execute("ALTER TABLE test ADD COLUMN IF NOT EXISTS city TEXT")