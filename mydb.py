# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector 

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Anderson438$'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create database 
cursorObject.execute("CREATE DATABASE IF NOT EXISTS djangoDb")

print("Database created")