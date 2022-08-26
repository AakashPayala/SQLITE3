import sqlite3

from pkg_resources import ContextualVersionConflict
conn = sqlite3.connect("customer.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE customers(
    name text,
    age text,
    height text,
    weight text
)
""")
cursor.execute(
    """INSERT INTO customers VALUES('aakash', '21','5 ft 6 inches ','55kg ')""")

val = [
    ('aakash', '21', '5 ft 6 inches ', '55kg '),
    ('aakash', '21', '5 ft 6 inches ', '55kg '),
    ('aakash', '21', '5 ft 6 inches ', '55kg '),
    ('aakash', '21', '5 ft 6 inches ', '55kg '),
    ('aakash', '21', '5 ft 6 inches ', '55kg '),
    ('aakash', '21', '5 ft 6 inches ', '55kg '),
    ('aakash', '21', '5 ft 6 inches ', '55kg '),
    ('aakash', '21', '5 ft 6 inches ', '55kg '),
    ('aakash', '21', '5 ft 6 inches ', '55kg '),
    ('aakash', '21', '5 ft 6 inches ', '55kg '),

]
cursor.execute("""SELECT * FROM customers""")


print(cursor.fetchall())

print("-------------------------------------------------")
cursor.executemany("""INSERT INTO customers VALUES(?,?,?,?)""", val)

cursor.execute("""SELECT rowid, * FROM customers""")

data = cursor.fetchall()
for i in data:
    print(i[0], " \t\t", i[1], "\t\t", i[2], "\t\t", i[3], "\t\t", i[4])

print("=====================================================================================================")
cursor.execute(
    """INSERT INTO customers VALUES('utkarsh','123','6ft 7inches','90kg')""")
cursor.execute("""SELECT rowid,* FROM customers""")
data2 = cursor.fetchall()
# print(data2)
for i in data2:
    print(i[0], " \t\t", i[1], "\t\t", i[2], "\t\t", i[3], "\t\t", i[4])

print("----------------------------------------------------------------------------------------")
cursor.execute("""UPDATE customers SET name='daksh' WHERE rowid=12""")
cursor.execute("""SELECT rowid,* FROM customers""")
data4 = cursor.fetchall()
# print(data2)
for i in data4:
    print(i[0], " \t\t", i[1], "\t\t", i[2], "\t\t", i[3], "\t\t", i[4])


print("------------------------------------------------------------------------------")

cursor.execute("""SELECT rowid, * FROM customers WHERE weight=='55kg'""")
data3 = cursor.fetchall()
for i in data3:
    print(i[0], " \t\t", i[1], "\t\t", i[2], "\t\t", i[3], "\t\t", i[4])


cursor.execute("""DROP TABLE customers""")
conn.commit()
conn.close()


