#sqlite3
#pymysql
#pymongo


#connect("host","post","username","pass")#mysql
#connect()#mongodb#http//127.0.0.1.27017

import sqlite3
connection=sqlite3.connect("sample1.db")
cursor=connection.cursor()
# cursor.execute("create table student(rollno int,stname varchar,mark int);")
# cursor.execute("insert into student values(101,'durai',450);")
cursor.execute("insert into student values(102,'chella',459);")
cursor.execute("select * from student" )

print(cursor.fetchall())
# print(cursor.fetchone())
# print(cursor.fetchmany(10))

connection.commit()
connection.close()