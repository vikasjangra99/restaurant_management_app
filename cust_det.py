import sqlite3

conn=sqlite3.connect("database1.db")
# conn.execute("create table cust_det\
# (cust_id int primary key,\
# cust_name varchar(50) not null,\
# cust_mno int not null,\
# cust_add varchar(50) not null)")
# conn.execute("insert into cust_det values(2001,'Aniket',9876543210,'Mulund')")
conn.commit()
cursor=conn.execute("select * from cust_det")
print(cursor.fetchall())
