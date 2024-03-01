#Display the contents of a table 
import mysql.connector as ps

try:
    cn=ps.connect(host='localhost',
                  port=3306,user='root',password='1234',db='studentdb')
    
    cmd=cn.cursor()
    
    query="select * from student_table"
    
    cmd.execute(query)
    
    rows=cmd.fetchall()
    
    # print(rows)
    for row in rows:
        for col in row:
            print(col,end=' ')
        print()
    
    cn.close()

except Exception as e:
    print(e)
