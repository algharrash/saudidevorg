#week 11 challenge

import mysql.connector

#part one
f = open("chtxt.txt", "rt")
print(f.read())
f.close()

f = open("chtxt.txt", "a")
f.write("The best way we learn anything is by practice and exercise questions")
f.close()

f = open("chtxt.txt", "rt")
print(f.read())
f.close()

#part two
mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    passwd = ""
)

myc = mydb.cursor()
myc.execute("CREATE DATABASE IF NOT EXISTS MyEmployee")
myc.execute("USE MyEmployee")
myc.execute("CREATE TABLE Employee (id INT AUTO_INCREMENT PRIMARY KEY, FirstName VARCHAR(255), LastName VARCHAR(255), Age INT, Gender VARCHAR(255), Salary INT)")
sql = "INSERT INTO Employee (FirstName, LastName, Age, Gender, Salary) VALUES (%s, %s, %s, %s, %s)"
val = [
    ("Ahmad", "Ali", 30, "Male", 10000),
    ("Khalid", "Muhammad", 34, "Male", 7000),
    ("Norah", "Saleh", 29, "Female", 7000)
]
myc.executemany(sql, val)


myc.execute("SELECT * FROM Employee")
result = myc.fetchall()

print("Display Employee Table Content:")
for x in result:
    print(x)

myc.execute("SELECT FirstName, Gender, Salary FROM Employee")
result = myc.fetchall()

print("Display Employee Table Columns (FirstName, Gender, Salary) Content:")
for x in result:
    print(x)

myc.execute("SELECT * FROM Employee ORDER BY FirstName  DESC")
result = myc.fetchall()

print("Display Employee Table Content order bay FirstName Decending order:")
for x in result:
    print(x)

myc.execute("DELETE FROM Employee WHERE Age = 34")
myc.execute("SELECT * FROM Employee")
result = myc.fetchall()

print("Display Employee Table Content After Delecting Column that has Age = 34:")
for x in result:
    print(x)



