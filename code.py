import mysql.connector
mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlroot",
    database="project"
)

cursor=mydb.cursor()
# print(mydb)

# Show existing tables
cursor.execute("SHOW TABLES")
 
for x in cursor:
  print(x)
# cursor.execute("SHOW TABLES")
# for x in cursor:
#     print(x)

#SQL 
# LOAD DATA LOCAL INFILE '/Users/riteshbhandari/Desktop/Rests.csv'
# INTO TABLE Restraunt1
# FIELDS TERMINATED BY ','
# ENCLOSED BY '"'
# LINES TERMINATED BY '\n'
# IGNORE 1 ROWS;