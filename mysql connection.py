# MYSQL CONNECTIVITY WITH PYTHON

# pip install mysql-connector-python
import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",password="",db="assignments")
cur = con.cursor()

empId = int(input("Enter EmpID : "))
empName = input("Enter EmpName : ")
salary = int(input("Enter Salary :  "))
query = "insert into employee (empId,empName,Salary,DeptId,JoinDate,Email) values (%s,%s,%s,%s,%s,%s)"
# cur.execute(query)
# con.commit()#delete,update,insert-to save all the changes
# query = "delete from employee where empId=110"
# cur.execute(query)
con.commit()

cur.execute("select * from employee")
for data in cur.fetchall():
    print(data)

