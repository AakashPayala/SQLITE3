from cgitb import text
from contextlib import nullcontext
import sqlite3
# connect to database if not available create one 
conn=sqlite3.connect("database.db")
cur=conn.cursor()

# creating a table
cur.execute("""CREATE TABLE customers
    (first_name text,
    last_name text,
    email text)
    """)
#insert a value into the table 
cur.execute("INSERT INTO customers VALUES('Aakash','Payala','akash01@gmail.com')")
many_customers=[("one","two","three"),
                ("four","five","six"),
                ("seven","eight","nine")]
cur.executemany("INSERT INTO customers VALUES(?,?,?)",many_customers)
# diff data types in sqlite3
# text
# null
# blob
# integers
# real

cur.execute("INSERT INTO customers VALUES('this','is','new')")
#printing

cur.execute("""UPDATE customers SET first_name='lakshy' WHERE rowid=1""")
cur.execute("SELECT * FROM customers")
print(cur.fetchall()) 



# commiting changes 
conn.commit()
print ("success")

# close our connection 
conn.close()