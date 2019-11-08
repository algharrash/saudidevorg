#handling database in python

import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    passwd = ""
)

myc = mydb.cursor()
myc.execute("CREATE DATABASE mydb")

myc.execute("SHOW DATABASES")

for x in myc:
    print(x)

