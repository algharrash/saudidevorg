#handling database in python

import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    passwd = "",
    database = "mydb"
)

myc = mydb.cursor()
myc.execute("CREATE TABLE courses (id INT AUTO_INCREMENT PRIMARY KEY, code VARCHAR(255), name VARCHAR(255))")

sql = "INSERT INTO courses (code, name) VALUES (%s, %s)"
val = [
    ("COE 202", "Digital Logic Design"),
    ("COE 203", "Digital Logic Design Lab"),
    ("COE 241", "Data and Computer Communications"),
    ("COE 300", "Principles of Computer Engineering Design"),
    ("COE 301", "Computer Organization"),
    ("COE 344", "Computer Networks")
]

myc.executemany(sql, val)
mydb.commit()

print(myc.rowcount, "record was inserted.")

myc.execute("SELECT * FROM courses")
result = myc.fetchall()

for x in result:
    print(x)


