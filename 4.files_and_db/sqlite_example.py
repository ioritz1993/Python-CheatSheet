import sqlite3
import os

pathDatabase = "files/sqlite_example"

if os.path.isfile(pathDatabase):
    os.remove(pathDatabase)

database_connection = sqlite3.connect(pathDatabase)

cursor = database_connection.cursor()

cursor.execute('''
    CREATE TABLE EXAMPLE(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Property1 VARCHAR(200) UNIQUE,
        Property2 INTEGER NOT NULL,
        Property3 VARCHAR(200))
''')

example_list = [
    ("Article1", 43, "Example1"),
    ("Article2", 223, "Example2"),
    ("Article3", 633, "Example3")
]
try:
     cursor.execute("INSERT INTO EXAMPLE VALUES (NULL,'Value1', 345, 'Value2')")
     cursor.executemany("INSERT INTO EXAMPLE VALUES (NULL,?,?,?)", example_list)
     cursor.execute("SELECT * FROM EXAMPLE")
     data = cursor.fetchall()
     print(data)

     database_connection.commit()
finally:
    database_connection.close()