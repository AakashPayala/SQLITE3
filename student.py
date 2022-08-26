import sqlite3

conn=sqlite3.connect('academic_detail.db')

c=conn.cursor()

c.execute("""CREATE TABLE students(
    reg_no text,
    attendance integer,
    grade text,
    name text
    )""")

details=[('ra748',67,'D','aakash'),
('ra234',76,'A','sfho'),
('ra234',89,'C','rghe'),
('ra984',73,'B','Georgre')]

c.executemany("""INSERT INTO students VALUES(?,?,?,?)""",details)


c.execute("""SELECT * FROM students""")
# print("reg no \t attendance\tgrade \t name")
d=c.fetchall()
for i in d:
    print(i[0],"\t",i[1],"\t",i[2],"\t\t",i[3])

print("==============================================")

c.execute("""SELECT * FROM students WHERE attendance<75""")

s=c.fetchall()
for i in s:
    print(i[0],"\t",i[1],"\t",i[2],"\t\t",i[3])


print("==========================================================")

c.execute("""SELECT * FROM students""")
ha=c.fetchall()
highest=0
for i in ha:
    if(i[1]>highest):
        highest=i[1]


print("highest att-> ",highest)


print("=============================================================")

c.execute(""" UPDATE students SET name='Jhon' WHERE name='Georgre'""")


c.execute("""SELECT * FROM students""")
# print("reg no \t attendance\tgrade \t name")
up=c.fetchall()
for i in up:
    print(i[0],"\t",i[1],"\t",i[2],"\t\t",i[3])
print("===================================================================")
c.execute("""DELETE FROM students WHERE reg_no='ra748'""")
c.execute("""SELECT * FROM students""")
# print("reg no \t attendance\tgrade \t name")
up=c.fetchall()
for i in up:
    print(i[0],"\t",i[1],"\t",i[2],"\t\t",i[3])

conn.commit()
conn.close()

