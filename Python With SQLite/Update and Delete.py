import sqlite3

con = sqlite3.connect("updatedelete.db")
cus = con.cursor()

cus.execute("CREATE TABLE IF NOT EXISTS ud(name TEXT,city TEXT)")
cus.execute("INSERT INTO ud VALUES ('abc','xyz')")
cus.execute("INSERT INTO ud VALUES ('pqr','mno')")
cus.execute("INSERT INTO ud VALUES ('opq','fgh')")
cus.execute("SELECT * FROM ud")
for rows in cus.fetchall():
    print(rows)
print("---------------------------")

name = input("enter name for update name where name=pqr :- ")
city = input("enter city for update city where name=pqr :- ")

cus.execute("UPDATE ud SET name=(?),city=(?) WHERE name='pqr'", (name, city))

cus.execute("SELECT * FROM ud")
for rows in cus.fetchall():
    print(rows)
print("---------------------------")
con.commit()

namedel = input("enter city name you want to delete :- ")


cus.execute("DELETE FROM ud WHERE city=(?)",(namedel,))
cus.execute("SELECT * FROM ud")
for rows in cus.fetchall():
    print(rows)
print("---------------------------")

cus.execute("DROP TABLE ud")

con.commit()
cus.close()
con.close()