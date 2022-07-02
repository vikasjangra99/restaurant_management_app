import sqlite3

conn=sqlite3.connect('database1.db')
# conn.execute("create table emp_det\
# ( emp_id int primary key,\
# emp_name varchar(50) not null,\
# emp_no int not null,\
# emp_add varchar(100) not null,\
# emp_dob varchar(50),\
# emp_email varchar(50),\
# emp_password varchar(50)\
# )\
# ")
# conn.execute("insert into emp_det values(1001,'Omkar',9999999999,'Mulund','6-6-1998','omkar661998@gmail.com','omkar1234')")
# conn.commit()
# cursor=conn.execute("select * from emp_del where emp_name='Omkar' and emp_dob='6-6-1998' and emp_add='Mulund'")


# cursor=conn.execute("select * from emp_det where emp_email='omkar661998@gmail.com'")
cursor=conn.execute("select * from emp_det")
print(cursor.fetchall())
conn.close()
