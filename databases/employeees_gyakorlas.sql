
-- 1. Válassz ki minden olyan dolgozót akinek a keresztneve "Elvis"

select first_name, last_name
from employees.employees
where first_name = 'Elvis';

-- 2. Válassz ki minden olyan női dolgozót akinek a keresztneve Kellie

select gender, first_name as name
from employees.employees
where gender = 'f' and first_name = 'Kellie';

-- 3. Válassz ki minden olyan dolgozót akinek a keresztneve Kellie vagy Aruna

select emp_no, first_name as name
from employees.employees
where first_name = 'Aruna' or first_name = 'Kellie';

-- 4. Válassz ki minden olyan dolgozót az IN segítségével, akinek a keresztneve Denis vagy Elvis.

select emp_no, first_name as name
from employees.employees
where first_name in ('Denis', 'Elvis');

-- 5. Keress ki minden olyan dolgozót akinek a keresztneve John, Mark, vagy Jacob

select first_name as name
from employees.employees
where first_name in ('John', 'Mark', 'Jacob');

-- 6. Keress ki minden olyan dolgozót aki a 2000-es évben lett felvéve

select first_name, last_name, hire_date
from employees.employees
where hire_date BETWEEN "2000-01-01" and "2000-12-31";

select first_name, last_name, hire_date
from employees.employees
where hire_date like "2000%";

-- 7. Keress ki minden olyan dolgozót akinek a employee number-je 5 karakterből áll és 1000-el kezdődik

select first_name, last_name, emp_no
from employees.employees
where length(emp_no) = 5 and emp_no like "1000%";

select first_name, last_name, emp_no
from employees.employees
where emp_no like "1000_";

-- 8. Keress ki minden olyan dolgozót akinek a keresztneve tartalmazza a "Jack" szót

select emp_no, first_name as name
from employees.employees
where first_name like "%jack%";

-- 9. Válassz ki minden információt a salaries table-ből de csak azok a
-- fizetések kellenek amelyek 66 000 és 70 000 közé esnek, csak az első 10 találatot kérdezd le!

select * from employees.salaries
where salary between 66000 and 70000
limit 10;

-- 10. Keresd ki azokat a dolgozókat akiknek az azonosító száma nem 10004 és 10012 közé esik, limitáld
-- a találatok számát az első 100ra

select *
from employees.employees
where emp_no not between '1004' and '10012'
limit 100;


-- 11. Keresd ki azokat az osztályokat (departments) ahol az azonosító szám d003 vagy d006 

select dept_name, dept_no
from employees.departments
where dept_no = "d003" or dept_no = "d006";

-- ha két érték közötti értékeket szereténk:
select dept_name, dept_no
from employees.departments
where dept_no between "d003" and "d006";

-- 12. Keresd ki azokat az osztályokat (departments) amelyeknek az azonsító száma nem null 

select dept_no, dept_name
from employees.departments
where dept_no is not null;

-- 13. Keresd ki az összes női dolgozóról minden adatot, akik 2000 január 1-e
-- után lettek felvéve vagy aznap, limitáld a sorokat 10re!

select * from employees.employees
where gender = "f" and hire_date like "20%"
limit 10;

select * from employees.employees
where gender = "f" and hire_date >= '2000-01-01'
limit 10;

-- 14. Keress ki minden dolgozót akinek 150 000 -nél nagyobb a fizetése,
-- limitáld az első 100 találatig

select * from employees.salaries
where salary > 150000
limit 100;

-- 15. Keress ki minden egyedi munkába állási dátumot az employees táblából, de
-- csak az els 10et jelenitsd meg

select distinct hire_date 
from employees.employees
limit 10;

-- 16. mennyi olyan eset volt a salaries táblában amikor 100 000-nél nagyobb fizetést vittek fel

select count(salary)
from employees.salaries
where salary > 100000;

-- 17. Mennyi manager van az employees adatbázisban? 

select count(*)
from employees.dept_manager;


-- 18. Válassz ki minden adatot az employees táblából, hire_date szerint csökkenő sorrendbe, és csak az első
-- 10 találatot irasd ki -- Sanyi

select * from employees.employees
order by hire_date desc
limit 10;

-- 19. Írj egy lekérdezést ami két oszlopot fog megjeleníteni. Az egyik oszlop azokat a fizetéseket listázza ahol az összeg nagyobb mint 80 000
-- A második oszlop neve emps_with_same_salary legyen amely azt mutassa hogy hány olyan dolgozó van akinek ilyen fizetése van.
-- Rendezd a kimenetet az első oszlop szerint. 

select salary, count(emp_no) as emps_with_same_salary
from employees.salaries
where salary > 80000
group by salary
order by salary
limit 100;


-- 20. Válassz ki minden dolgozót (elég az emp_no) akinek az átlag fizetése nagyobb mint 120 000. 

select emp_no, avg(salary) as avg_salary
from employees.salaries
group by emp_no
having avg(salary) > 120000
order by emp_no
limit 10;

-- 21. Válasszd ki azokat az emp_no-eket akik több mint egy szerződést írtak
-- alá, 2000 január elseje után Segítség: használd a dept_emp táblát.  - Beni

select emp_no
from employees.dept_emp
where from_date > '2000-01-01'
group by emp_no
having count(from_date) > 1;

-- 22. Összesen mennyi részleg van az employees adatbázisban?
-- Használd a dept_emp táblát a kérdés megválaszolásához - Sándor

select count(distinct dept_no)
from employees.dept_emp;

-- 23. Összesen mennyi pénzt költöttek fizetésre 1997 január elseje
-- óta? - Nóra

select sum(salary)
from employees.salaries
where from_date > '1997-01-01';

-- 24. Melyik a legalacsonyabb számu employee number az
-- adatbázisban? - Sándor

select min(emp_no)
from employees.employees;

-- 25. Melyik a legmagasabb számu employee number az adatbázisban? - Beni

select max(emp_no)
from employees.employees;

-- 26. Átlagosan mennyi fizetést költöttek 1997-01-01 óta ? - Nóra

select avg(salary)
from employees.salaries
where from_date > '1997-01-01';

-- 27. Kerekítsd kettő tizedesjegyre az átlagfizetést 1997-01-01
-- óta! - Sandor

select round(avg(salary), 2) as avg_salary
from employees.salaries
where from_date > '1997-01-01';

-- 28. Válaszd ki a részleg számot (department number) és a részleg
-- nevét a departments táblából és adj hozzá egy harmadik oszopot
-- amely a dept_info nevet kapja. Ha a dept_no üres akkor a dept_name
-- kerüljön ebbe az oszlopba  - Nóra

select dept_no, dept_name, coalesce(dept_no, dept_name) as dept_info
from employees.departments
order by dept_no asc;

-- 29. Keress ki minden információt a manager-ekről. Employee
-- number, vezetéknév, keresztnév, részleg szám, és hire date. - Beni

select emp_no, last_name, first_name, dept_no, hire_date
from employees.dept_manager
inner join employees.employees using(emp_no);

-- 30. egyesítsd az employees és a dept_manager táblát és listázz ki minden
-- olyan employee-t akinek a keresztneve Markovitch. Nézd meg van e a
-- kimenetben manager ezzel a névvel.  segítség: ezeket a field-eket válaszd
-- ki: ‘emp_no’, ‘first_name’, ‘last_name’, ‘dept_no’, ‘from_date’. rendezz
-- 'dept_no' szerint csökkenőbe aztán 'emp_no' szerint. --- Beni

select emp_no,
first_name,
last_name,
dept_no,
from_date
from employees.employees
left join employees.dept_manager using(emp_no)
where last_name = 'markovitch'
order by dept_no desc, emp_no;


-- 31. Válaszd ki azokat a first_name, last_name, hire_date, title oszlopokat
-- akiknél a keresztnév "margareta" és a vezetéknév "markovitch" - Sandor

select first_name,
last_name,
hire_date,
title
from employees.employees
inner join employees.titles using(emp_no)
where first_name = 'margareta' and last_name = 'markovitch';

-- 32. Válassz ki minden managert úgy hogy ezek a mezők legyenek az
-- eredményben: first and last name, hire date, job title, start date, and
-- department name. - Nora

select first_name,
last_name,
hire_date,
title,
dept_manager.from_date,
dept_name
from employees.dept_manager
join employees.employees using(emp_no)
join employees.titles using(emp_no)
join employees.departments using(dept_no)
where title = 'manager';


-- 33. Keress ki minden információt a department manager-ekeről akik 1990-01-01
-- és 1995-01-01 között lettek felvéve. (Subquery)

select * 
from employees.dept_manager
where emp_no in (
  select emp_no
  from employees.employees
  where hire_date between '1990-01-01' and '1995-01-01'
);

