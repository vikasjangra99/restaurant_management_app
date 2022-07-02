import sqlite3

# Create a SQL connection to our SQLite database
database = "database1.db"
con = sqlite3.connect(database)

cur = con.cursor()

# The result of a "cursor.execute" can be iterated over by row
for row in cur.execute('SELECT * FROM cust_det;'):
    print(row)

# Be sure to close the connection
con.close()
