
-- view

create or replace view employees.v_department_emp_latest_date as
select emp_no, max(from_date) as from_date, max(to_date) as to_date
from employees.dept_emp
group by emp_no
limit 10;

select * from employees.v_department_emp_latest_date;

-- stored procedure
use employees;
drop procedure if exists select_employees;

delimiter $$
create procedure select_employees()
begin
  select * from employees
  limit 100;
end$$
delimiter ;

call employees.select_employees();

-- stored procedure with input parameter

use employees;
drop procedure if exists emp_salary;

delimiter $$
create procedure emp_salary(in p_emp_no integer)
begin
  select first_name, last_name, salary, from_date, to_date
  from employees.employees
  inner join employees.salaries using(emp_no)
  where employees.emp_no = p_emp_no;
end$$
delimiter ;

call employees.emp_salary(11330);

-- stored procedure with input and output parameter


use employees;
drop procedure if exists emp_avg_salary_out;

delimiter $$
create procedure emp_avg_salary_out(in p_emp_no integer, out p_avg_salary decimal(10, 2))
begin
  select avg(salaries.salary) into p_avg_salary
  from employees.employees
  inner join employees.salaries using(emp_no)
  where employees.emp_no = p_emp_no;
end$$
delimiter ;


-- változó létrehozása:
set @v_avg_salary = 0;
call employees.emp_avg_salary_out(11330, @v_avg_salary);
select @v_avg_salary;

-- stored function

use employees;
drop function if exists f_emp_avg_salary;

delimiter $$
create function f_emp_avg_salary(p_emp_no integer) returns decimal(10,2)
begin
  -- fuggvényen belül lokális változót nem a set szóval hanem a declare szóval csinálunk
  -- és nemkell a @ jel
  declare v_avg_salary decimal(10, 2);

  select avg(salaries.salary) into v_avg_salary
  from employees.employees
  inner join employees.salaries using(emp_no)
  where employees.emp_no = p_emp_no;
 
  -- ezt ha kihagynánk errort dobna az sql mert a függvény létrehozásakor
  -- megmondtuk hogy ez a függvény visszaad valamit
  return v_avg_salary;

end$$
delimiter ;

select employees.f_emp_avg_salary(11300);

-- procedure-nak lehet több out paramétere is, function-nek csak egy lehet
-- a functionnek mindig kell hogy legyen return értéke (insert, update delete
-- műveleteket fügvénnyel nem lehet csinálni)

-- call procedure;
-- select function;

-- funciton-t tudunk használni select statement-en belül is, procedure-t nem

select * from employees.salaries
where salary > employees.f_emp_avg_salary(11300)
limit 10;

use employees;
set @v_emp_no = 11300;
select emp_no, first_name, last_name, f_emp_avg_salary(@v_emp_no) as avg_salary
from employees
where emp_no = @v_emp_no;

-- global változók: mindenhol elérhetőek
set global max_connection = 1000;
-- vagy ígyis lehet írni:
set @@global.max_connections = 1;

-- összes változó lekérdezése;
show variables;
