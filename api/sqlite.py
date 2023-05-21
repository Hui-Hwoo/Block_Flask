# ------------------------------- #
#            Rest API             #
#     using SQLite as database    #
# ------------------------------- #
# https://www.tutorialspoint.com/sqlite/sqlite_python.htm
import os
import sqlite3

os.makedirs("./database/sqlite/", exist_ok=True)

conn = sqlite3.connect("./database/sqlite/items.db")

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3], "\n")
conn.close()


conn.execute(
    """CREATE TABLE IF NOT EXISTS COMPANY 
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);"""
)

conn.execute(
    "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )"
)

conn.execute(
    "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )"
)

conn.execute(
    "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )"
)

conn.execute(
    "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )"
)

conn.commit()

print("Opened database successfully")
