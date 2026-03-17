use assignments;

select max(salary) as "Maximum Salary",min(salary) as "Minimum Salary",avg(salary) as "Average Salary" from employee;

select * from employee;


-- table cloning 
create table deptDetails as
select deptName ,  count(DeptName) from employee as e inner join department as d on e.deptId=d.deptID group by deptName;

select * from deptDetails;


-- TCL - Transaction Control Language
create database payment;
use payment;
create table upi( pid int primary key auto_increment ,name text, amount int);

start transaction;
-- sahil sent 55000 in ragu's account 

savepoint s1;
insert into upi (name,amount) values ("RAGU",55000);


select * from upi;

rollback to s1;

