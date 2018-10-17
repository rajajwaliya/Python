import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", passwd="", database="testdb",buffered=True)
cus = con.cursor()

name = input("enter your name :- ")
city = input("enter your value :- ")
query1 = "INSERT INTO test (name,city) VALUES (%s,%s)"
query2 = (name, city)
cus.execute(query1, query2)
print("data insert at id :-",cus.getlastrowid())
con.commit()

print("------------------")
#insert multiple values

query1="INSERT INTO test (name,city) VALUES (%s,%s)"
query2=[('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),]

cus.executemany(query1,query2)
con.commit()
print(cus.rowcount,"rows insert successfully")

cus.close()
con.close()