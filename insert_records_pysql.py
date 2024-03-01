#To insert record/records in MySQL table via Python
#---------------------------INSERT----------------------------
import mysql.connector

cn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="studentdb"
)

cmd = cn.cursor()

sql = "INSERT INTO student2 (name, class, age ) VALUES (%s, %s, %s)"
val = ("Jane","fycs", 23)

try:  
  cmd.execute(sql, val)
  print(cmd.rowcount, "record inserted successfully.")
except:
  print('Something went wrong.')

cn.commit()

query2="select * from student2"

cmd.execute(query2)

rows=cmd.fetchall()
    
# print(rows)
for row in rows:
    for col in row:
        print(col,end=' ')
    print()
'''
'''
#------------------------------Insert Multiple---------------------
import mysql.connector

cn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="studentdb"
)

cmd = cn.cursor()


sql = "INSERT INTO student2 (name, class, age ) VALUES (%s, %s, %s)"
val = [
  ("Matt", "syit",232),
  ("Ethan", "fyit",12),
  ("Gina", "fycs",25)
]

try:  
  cmd.executemany(sql, val)
  print(cmd.rowcount, "records inserted.")
except:
  print('Something went wrong.')

cn.commit()
