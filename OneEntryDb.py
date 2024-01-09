import sqlite3

#!Connect(Create) to a DB and pass to variable connection
conn = sqlite3.connect("sql.db")      #sqlite3.connect("sql.db")

#!Create a cursor
curs = conn.cursor()

#!Create a "people" table
#   SQLITE3 |   PYTHON
#   INTEGER |   INT
#   REAL    |   FLOAT
#   TEXT    |   STRING
#   BLOB    |   BYTES
#   NULL    |   NONE 
curs.execute('''CREATE TABLE IF NOT EXISTS people(first_name TEXT, last_name TEXT)''')

#!Close Connection
curs.close()
conn.close()                          #sqlite3.connect("sql.db").close()