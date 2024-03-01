#Basic program to connect python to mysql and display databases
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234"
)

mycursor = mydb.cursor()
#Return a list of your system's databases:
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
