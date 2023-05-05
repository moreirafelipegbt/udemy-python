import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='my_database'
)

my_cursor = mydb.cursor()

#my_cursor.execute("CREATE TABLE student(name VARCHAR(255), age TINYINT, address VARCHAR(255))")
#my_cursor.execute("SHOW TABLES")

#for table in my_cursor:
#    print(table)

#sql_statement = 'INSERT INTO student(name, age, address) VALUES(%s, %s, %s)'
#values = ('Kevin', 34, '50447, 180 Jenna Lane')
#my_cursor.execute(sql_statement, values)
#mydb.commit()

#my_cursor.execute("SELECT * FROM student")
#result = my_cursor.fetchall()

#for row in result:
#    print(row)

#my_cursor.execute('UPDATE student SET age=32  WHERE name="Kevin"')
#mydb.commit()

#my_cursor.execute('SELECT * FROM student')
#result = my_cursor.fetchall()

#for row in result:
#    print(row)

my_cursor.execute("DELETE FROM student WHERE name='Kevin'")
mydb.commit()

my_cursor.execute('SELECT * FROM student')
result = my_cursor.fetchall()

for row in result:
    print(row)