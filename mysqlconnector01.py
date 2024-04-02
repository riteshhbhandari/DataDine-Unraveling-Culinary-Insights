#testing if mysql connector works
import mysql.connector
mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlroot",
    database="project"
)

cursor=mydb.cursor()
cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)