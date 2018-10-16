import sqlite3

con = sqlite3.connect("Test.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS TestDb (id INTEGER PRIMARY KEY,name TEXT,city TEXT )")
cur.execute("INSERT INTO TestDb(name,city) VALUES ('ABCD','bhavnagar')")

cur.execute("SELECT * FROM TestDb")
for raws in cur.fetchall():
    print(raws)
print("----------------")

cur.execute("SELECT * FROM TestDb WHERE name='raj'")
for raws in cur.fetchall():
    print(raws)
print("----------------")

cur.execute("SELECT name,id FROM TestDb WHERE city='bhavnagar'")
for raws in cur.fetchall():
    print(raws)
print("----------------")

cur.execute("SELECT * FROM TestDb WHERE city='bhavnagar'")
for raws in cur.fetchmany(3):
    print(raws[1],raws[2])
print("----------------")

