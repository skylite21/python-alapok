
select emp_no, first_name, last_name,
case
  when gender = 'M' then 'Male'
  else 'Female'
end as gender
from employees.employees
limit 20;

select emp_no, first_name, last_name,
max(salaries.salary) - min(salaries.salary) as salary_difference,
case
  when max(salaries.salary) - min(salaries.salary) > 30000 then 'A fizetésemelés több volt mint $30 000'
  when max(salaries.salary) - min(salaries.salary) between 20000 and 30000 then 'A fizetésemelés 20 és 30e között'
  else 'A fizetés kevesebb mint 20e-el nőtt'
end as salary_increase
from employees.dept_manager
inner join employees.employees using(emp_no)
inner join employees.salaries using(emp_no)
group by salaries.emp_no;

