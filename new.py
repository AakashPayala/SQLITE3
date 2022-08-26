
from distutils.sysconfig import customize_compiler
import sqlite3


connection=sqlite3.connect("company.db")

cursor=connection.cursor()
cursor.execute("""CREATE TABLE employees
(
    employee_id text,
    first_name text,
    last_name text,
    job_id text,
    salary integer
)""")

# text
# Blob 
# real
# integer 
# null
cursor.execute("""INSERT INTO employees VALUES('ra748','aakash','payala','60A',2312)""")
var=[('ra234','aa','ll','234',3274),
    ('ra123','df','53','2312213',300),
    ('ra234v','adva','ll21','344',466),
    ('ra23e4','aeea','leefl','2234',11324)]

cursor.executemany("""INSERT INTO employees VALUES(?,?,?,?,?)""",var)

cursor.execute("""SELECT * FROM employees""")
# print(cursor.fetchall())
temp=cursor.fetchall()
print(" employee_id|\t|first_name|\t|last_name|\t|job_id|\t|salary")
for i in temp:
    print(i[0]+"\t\t"+i[1]+"\t\t"+i[2]+"\t\t"+i[3]+"\t\t"+str(i[4]))
print("============================================================================")
cursor.execute("""SELECT * FROM employees WHERE salary>1000""")
temp1=cursor.fetchall()
print(" employee_id|\t|first_name|\t|last_name|\t|job_id|\t|salary")
for i in temp1:
    print(i[0]+"\t\t"+i[1]+"\t\t"+i[2]+"\t\t"+i[3]+"\t\t"+str(i[4]))

print("============================================================================")
cursor.execute(""" UPDATE employees SET first_name='utkarsh' WHERE rowid=2""")
cursor.execute("""UPDATE employees SET last_name='betichod' WHERE rowid=2""")
cursor.execute("""SELECT * FROM employees""")
temp1=cursor.fetchall()
print(" employee_id|\t|first_name|\t|last_name|\t|job_id|\t|salary")
for i in temp1:
    print(i[0]+"\t\t"+i[1]+"\t\t"+i[2]+"\t\t"+i[3]+"\t\t"+str(i[4]))
print("ok")

print("============================================================================")
cursor.execute("""DELETE FROM employees WHERE first_name='aakash'""")
cursor.execute("""SELECT * FROM employees""")
temp1=cursor.fetchall()
print(" employee_id|\t|first_name|\t|last_name|\t|job_id|\t|salary")
for i in temp1:
    print(i[0]+"\t\t"+i[1]+"\t\t"+i[2]+"\t\t"+i[3]+"\t\t"+str(i[4]))



print("============================================================================")

cursor.execute("""SELECT * FROM employees ORDER BY first_name LIMIT 1""")
temp1=cursor.fetchall()
print(" employee_id|\t|first_name|\t|last_name|\t|job_id|\t|salary")
for i in temp1:
    print(i[0]+"\t\t"+i[1]+"\t\t"+i[2]+"\t\t"+i[3]+"\t\t"+str(i[4]))
connection.commit()

connection.close()