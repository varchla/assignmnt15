#ques 1

import sqlite3
conn=sqlite3.connect("test.db")
print("opened database successfully")
conn.execute('''CREATE TABLE BOOK3
            (BOOK ID INT PRIMARY KEY NOT NULL,
            TITLE ID INT NOT NULL,
            LOCATION VARCHAR NOT NULL,
            GENRE TEXT)''')
print("table1 created successfully")

conn.execute('''CREATE TABLE TITLES
            (TITLE ID INT PRIMARY KEY NOT NULL,
             TITLE TEXT NOT NULL,
             ISBN VARCHAR NOT NULL,
             PUBLISHER ID INT NOT NULL,
             PUBLICATION YEAR INT NOT NULL)''')
print("table 2 created successfully")

conn.execute('''CREATE TABLE PUBLISHERS
            (PUBLISHER ID INT PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL,
            STREET ADDRESSS VARCHAR NOT NULL,
            ZIPCODE ID INT NOT NULL)''')
print("table3 created successfully")

conn.execute(''' CREATE TABLE ZIPCODES
             (ZIPCODE ID INT PRIMARY KEY NOT NULL,
             CITY VARCHAR NOT NULL,
             STATE VARCHAR NOT NULL,
             ZIPCODE VARCHAR NOT NULL)''')
print("table4 created successfully")

conn.execute(''' CREATE TABLE AUTHORTITLE
             (AUTHOR TITLE ID INT PRIMARY KEY NOT NULL,
              AUTHORID INT NOT NULL,
              TITLE ID INT NOT NULL)''')
print("table5 created successfully")

conn.execute(''' CREATE TABLE AUTHORS
            (AUTHOR ID INT NOT NULL,
             FIRST NAME VARCHAR NOT NULL,
             MIDDLE NAME VARCHAR NOT NULL,
             LAST  NAME VARCHAR NOT NULL)''')
print("table 6 created successfully")



conn.execute("INSERT INTO BOOK3(BOOK ID,TITLE ID,LOCATION,GENRE)\
              values(123,34,'DELHI','PHYSICS')")
conn.execute("INSERT INTO BOOK3(BOOK ID,TITLE ID,LOCATION,GENRE)\
              values(234,45,'CHANDIGARH','CHEMISTRY')")
conn.commit()
print("Records created successfully")



conn.execute("INSERT INTO AUTHORS(AUTHOR ID,FIRST NAME,MIDDLE LAST NAME)\
             values(54,'VARCHLA','KOMA;','THAKUR')")
conn.execute("INSERT INTO AUTHORS(AUTHOR ID,FIRST NAME,MIDDLE NAME,LAST NAME)\
              values(78,'RAJ','DEEP','SINGH')")
conn.commit()
print("Records created successfully")


conn.execute("UPDATE BOOK3 set TITLE ID=8 where BOOK ID=55")
conn.commit()
print("total number of rows updated",conn.total_changes)

cursor=conn.execute("SELECT BOOK ID,TITLE ID,LOCATION,GENRE FROM BOOK3")
for row in cursor:
    print("BOOKID=",row[0])
    print("TITLEID=",row[1])
    print("LOCATION=",row[2])
    print("GENRE=",row[3], "\n")
print("operation done successfully")
conn.close