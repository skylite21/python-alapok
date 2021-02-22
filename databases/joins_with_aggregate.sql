
-- mennyi a nők és a férfiak átlagfizetése
select employees.gender, avg(employees.salaries.salary) as avarage_salary
from employees.employees
join employees.salaries using(emp_no)
group by gender;

-- ha egy olyan mezőt is beleveszünk a selectbe amin nincsen semmi aggregációs függvény
-- az csak egy érték, ezért ilyenkor a legelső értéket teszi be az SQL
select emp_no, employees.gender, avg(employees.salaries.salary) as avarage_salary
from employees.employees
join employees.salaries using(emp_no)
group by gender;
