

select first_name
from sakila.actor
group by first_name;


-- a group by ha csak arra van használva hogy egyedi elemeket jelítsen meg, 
-- akkor lassabb mint a distinct
select distinct first_name
from sakila.actor;

-- a group by akkor jó ha bármilyen összesítést csinálunk
-- (`aggregate` function-t használva)
select first_name, count(first_name)
from sakila.actor
group by first_name
order by count(first_name) desc;


select title from sakila.film
where release_year >= "2005";

-- ha a feltételben is van aggregate function akkor kell a HAVING-et használni
-- a where-t nem lehet...

select first_name, count(first_name) as name_count
from sakila.actor
group by first_name
having count(first_name) > 3;

-- a where a group by előtt kell hogy legyen, mert akkor történik meg, a having pedig
-- a group by után

select first_name, count(first_name) as name_count
from sakila.actor
where first_name like "j%"
group by first_name
having count(first_name) > 3;

