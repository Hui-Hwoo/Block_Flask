# ------------------------------- #
#            Rest API             #
#     using SQLite as database    #
# ------------------------------- #
# https://www.tutorialspoint.com/sqlite/sqlite_python.htm
import os
import sqlite3


# Connect SQLite
def get_database():
    # Create Folder to save files
    os.makedirs("./database/sqlite/", exist_ok=True)
    database = sqlite3.connect("./database/sqlite/items.db")
    print("Successfully connected to databse!")
    return database


# Implement Queries
def imp_queries(database, queries):
    for query in queries:
        cursor = database.execute(query)
    database.commit()
    return cursor
    # for row in cursor:
    #     print("ID = ", row[0])
    #     print("NAME = ", row[1])
    #     print("ADDRESS = ", row[2])
    #     print("SALARY = ", row[3], "\n"


if __name__ == "__main__":
    database = get_database()
