import mysql.connector

conn = mysql.connector.connect(username="root",database="st")
cursor = conn.cursor()

'''
query = "create table students(roll int primary key auto_increment,name text,class text,marks int)"
cursor.execute(query)
'''

text = '''
Press 1 to Enter New Record
Press 2 to Update Existing Record
Press 3 to See All Records
'''
choice = int(input(text))
if choice==1:
    name = input("Enter name : ")
    cls = input("Enter class : ")
    marks = int(input("Enter marks : "))
    values = [name,cls,marks]
    query = "insert into students (name,class,marks) values (%s,%s,%s)"
    cursor.execute(query,values)
    print("Record Successfully Saved✅")
   
elif choice==2:
    roll = int(input("Enter Roll No :"))
    marks = int(input("Enter New Marks : "))
    query = f"update students set marks={marks} where roll={roll}"
    cursor.execute(query)
    print("Record Updated✅")

elif choice==3:
    query = "select * from students"
    cursor.execute(query)
    for data in cursor.fetchall():
        print(data)

conn.commit()#to save the changes permanently
    
    
    
