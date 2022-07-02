import sqlite3

conn=sqlite3.connect("database1.db")
# conn.execute("create table history\
# (\
# order_no int primary key,\
# cust_id int,\
# item_nos varchar(200),\
# quantity varchar(200),\
# bill number\
# )")
# conn.execute("insert into history values(3001,2001,'1001 1002','4 2 2 1',1312.12)")

conn.commit()

cursor=conn.execute("select * from history")
print(cursor.fetchall())