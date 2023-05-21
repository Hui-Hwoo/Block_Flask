# ------------------------------- #
#            Rest API             #
#     with mySQL as database      #
# ------------------------------- #


# ========= Using mysql-connector-python ========= #
#  https://dev.mysql.com/doc/connector-python/en/  #

import os

import mysql.connector
from mysql.connector import errorcode

# from __future__ import print_function


# Connect to MySQL Database
def get_database():
    # Configure
    config = {
        "user": os.getenv("SQL_USER"),
        "password": os.getenv("SQL_PASSWORD"),
        "host": os.getenv("SQL_HOST"),
        "database": os.getenv("SQL_DATABASE_NAME"),
        "raise_on_warnings": True,
    }
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        cursor.execute(f"USE {config['database']}")
        print("Successfully connected to MySQL database!")
        return cnx, cursor
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
            exit(1)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print(f"Database {config['database']} does not exist")
            create_database(cursor)
            print(f"Database {config['database']} created successfully.")
            return get_database()
        else:
            print(err)
            exit(1)


# Create Database
def create_database(cursor, dbname):
    try:
        cursor.execute(f"CREATE DATABASE {dbname} IF NOT EXISTS DEFAULT CHARACTER SET 'UTF8MB3'")
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


# Implement Query Statement
def imp_query(cnx, cursor, query):
    try:
        result = cursor.execute(query)
        cnx.commit()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")
    return result


# Using PyMySQL
# https://pymysql.readthedocs.io/en/latest/
# https://pymysql.readthedocs.io/en/latest/modules/cursors.html

import pymysql.cursors

# Connect to the database
def get_database():
    cnx = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="block_flask",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )
    cursor = cnx.cursor()
    return cnx, cursor

def imp_query(cnx, cursor, query):
    cursor.execute(query)
    result = cursor.fetchone()
    cnx.commit()

    return result

# sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
# cursor.execute(sql, ("webmaster@python.org", "very-secret"))

        
        
