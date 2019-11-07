import sqlite3
from sqlite3 import Error

db=sqlite3.connect('studente.db')
print('connnection establlished')

poi=db.cursor()

def create_table():
    poi.execute("CREATE TABLE STUDENT (SID int primary key,NAME text,AGE int,Marks int)")
    db.commit()
    print("table created")

def value():
    poi.execute("INSERT INTO STUDENT(SID,NAME,AGE,MARKS) VALUES(2819,'SALONI',19,56)")
    poi.execute("INSERT INTO STUDENT(SID,NAME,AGE,MARKS) VALUES(2019, 'vijay',19,100)")
    poi.execute("INSERT INTO STUDENT(SID,NAME,AGE,MARKS) VALUES(0619, 'vandana',19,101)")
    poi.execute("INSERT INTO STUDENT(SID,NAME,AGE,MARKS) VALUES(0519, 'vinamra',25,102)")
    db.commit()

def display():
    print("all student data")
    val = poi.execute('SELECT * FROM STUDENT')
    for row in val:
        print('Student ID:', row[0])
        print('Student Name:', row[1])
        print('Student Age:', row[2])
        print('Student Marks:', row[3])
        print('')

def DisplayQuery():
    print('Students With Marks Less Than 75:')
    val = poi.execute('SELECT * FROM STUDENT WHERE marks<75')
    for row in val:
        print('Student ID:', row[0])
        print('Student Name:', row[1])
        print('Student Age:', row[2])
        print('Student Marks:', row[3])
        print('')

def update():
    poi.execute('UPDATE STUDENT SET name = "jasmine" where SID = 0519')
    db.commit()

def delete():
    poi.execute('DELETE FROM STUDENT WHERE SID = 2819')
    db.commit()

n=0

while n==0:
    try:
        create_table()
        value()
        display()
        DisplayQuery()
        update()
        display()
        delete()
        display()
    except Error as e:
        print(e)
        n=1
