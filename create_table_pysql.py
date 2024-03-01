#Creating a table in MySQL database via Python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="studentdb"
)

mycursor = mydb.cursor()

sql = "CREATE TABLE student2 (name VARCHAR(10),class VARCHAR(10),age INT)"
mycursor.execute(sql)
print('Table created successfully.')

mydb.commit()
