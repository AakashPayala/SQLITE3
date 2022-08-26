import sqlite3
connection=sqlite3.connect("database2.db")

cursor=connection.cursor()
cursor.execute("""CREATE TABLE record 
(student_name text,
roll_no text,
section text)
""")
cursor.execute("""INSERT INTO record VALUES('Aakash','01','A')""")
cursor.execute("""SELECT * FROM record""")
print(cursor.fetchall())
print("done")


var=[('utkarsh','23','H'),
('adarsh','28','R'),
('anupam','33','A2')]
cursor.executemany("""INSERT INTO record VALUES(?,?,?)""",var)



cursor.execute("SELECT * FROM record")
value_record=cursor.fetchall()
for i in value_record:
    print(i) 

connection.commit()
print(".....................")
# value_record1=cursor.fetchall()
# for i in value_record:
#     print(i)
# cursor.execute("""UPDATE record SET student_name='LAKSHY' WHERE section='H'""")
# cursor.execute("DELETE FROM record WHERE rowid=3")
# cursor.execute("SELECT * FROM record ORDER BY student_name DESC")
# cursor.execute("""UPDATE record SET student_name='LAKSHY' WHERE student_name='Aakash' OR roll_no='33'""")
cursor.execute("""DELETE FROM record WHERE student_name='anupam'""")

cursor.execute("""DROP TABLE record""")
cursor.execute("""SELECT * FROM record ORDER BY student_name LIMIT 1""")
value_record=cursor.fetchall()
for i in value_record:
    print(i)
connection.commit()


connection.close()