import sqlite3

#!Connect(Create) to a DB and pass to variable connection
conn = sqlite3.connect("sql.db")

#!Create a cursor
curs = conn.cursor()

#!Test Data
people_list = [("John", "Doe"),("Jane", "Smith"),("Bob", "Johnson"),("Alice", "Williams"),("Charlie", "Brown")]

#!Create a "people" table with multiple entries
curs.executemany('''INSERT INTO people(first_name, last_name) VALUES(?, ?)''', people_list)
conn.commit()

#!Close Connection
curs.close()
conn.close()                          