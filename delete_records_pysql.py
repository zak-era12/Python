#------------------Conditional delete--------------
import mysql.connector

cn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="studentdb"
)

cmd = cn.cursor()


try:
  cmd.execute("DELETE FROM student2 WHERE class='fycs'")
  print('Rows are successfully deleted.')
except:
  print('An exception occurred while deleting rows.')

cn.commit()
