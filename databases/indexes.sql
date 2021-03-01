
-- lekérdezés eddig tartott:   2.29 sec
select * from employees.employees
where hire_date > '1998-01-01';

-- ha csinálunk indexet egy oszlopbol akkor az a lekérdezés idejét
-- csökkentheti
create index i_hire_date on employees.employees(hire_date);

-- 0.71sec
select * from employees.employees
where first_name = 'Georgi' and last_name = 'Facello';

create index i_comosite on employees.employees(first_name, last_name);
drop index i_comosite on employees.employees;

show index from employees from employees;

-- nagy teljesítménynövekedést hozhat nagy adatmennyiség esetén
-- kis adatmennyiség esetén ronthat a sebességen
-- a primary key és a unique key, alapértelmezetten már indexek
