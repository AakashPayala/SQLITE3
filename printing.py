import sqlite3
conn=sqlite3.connect("database.db")
c=conn.cursor()
# c.execute("INSERT INTO customers VALUES('aakash','payala','aakash01payala')")
# c.execute("INSERT INTO customers VAlUES('and','my','school')")
# c.execute("SELECT rowid,* FROM customers WHERE last_name='payala'")
# c.execute("SELECT * FROM customers WHERE last_name LIKE '%la'")
var = c.fetchall()
# print(var)
# print(c.fetchmany(3))
# print(c.fetchone()[1])
print("first_name \tlast_name \t email")
for i in var:
    print (i)
conn.commit()
conn.close()
