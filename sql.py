import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute('''Insert Into STUDENT values('Groot','Artificial Intelligence','A',95)''')
cursor.execute('''Insert Into STUDENT values('Stylo','Data Science','B',93)''')
cursor.execute('''Insert Into STUDENT values('Darius','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Israr','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Galaxy','DEVOPS','A',35)''')
cursor.execute('''Insert Into STUDENT values('Breath','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Judi','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Sb3','Data Science','A',88)''')
cursor.execute('''Insert Into STUDENT values('Tuff','DEVOPS','A',40)''')
cursor.execute('''Insert Into STUDENT values('Goat','DEVOPS','A',10)''')

## Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()