

-- if a value within the first_name field appears in the table more than once
-- by using group by it will be displayed only in a single row
select first_name
from sakila.actor
group by first_name;

-- ez hasonlo a distrinct-hez csak máshogy van rendezve
-- ebben az esetben a group by lassabb mint a district
select distinct first_name
from sakila.actor;

-- ha bármilyen összesítést csinálunk, a group by lesz az eszközünk
-- érdemes mindig magát a mezőt is beletenni a select statement-be hogy látszon
-- a mezők értéke
select first_name, count(first_name)
from sakila.actor
group by first_name;

-- order by-t lehet haszálni a group by után
select first_name, count(first_name)
from sakila.actor
group by first_name
order by first_name desc;


select title
from sakila.film
where release_year >= "2005";


-- a having után lehet aggregate functiont használni a feltételben
-- a where után nem lehet

select first_name, count(first_name) as name_count
from sakila.actor
group by first_name
having count(first_name) > 3;

-- a where condition a group by előtt történik meg, a having a group by után

select first_name, count(first_name) as name_count
from sakila.actor
where first_name like "ju%"
group by first_name
having count(first_name) > 3;

-- ha aggregate functiont használunk akkor having-et használjuk hozzá, ha pedig nem használunk aggregate function-t akkor a where-t
-- having-et aggregate function nélkül használva hibát fogunk kapni.

-- https://www.w3resource.com/mysql/aggregate-functions-and-grouping/aggregate-functions-and-grouping-in-mysql.php
