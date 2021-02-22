

-- 1. Jelenítsd meg az összes szinész vezetéknevét és keresztnevét

select first_name, last_name
from sakila.actor;

-- 2. Jelenítsd meg az összes színész teljes nevét csupa nagybetűkkel, egyetlen
-- oszlopban.  az oszlop neve "Actor Name" legyen.

select upper(concat(first_name, ' ', last_name)) as 'Actor Name'
from sakila.actor;

-- 2.a Jelenítsd meg az azonosító, vezetéknév, és keresztnév értékeit annak a
-- színésznek akinek a keresztneve Joe

select actor_id, last_name, first_name
from sakila.actor
where first_name = 'Joe';

-- 2.b Találj meg minden színészt akinek a vezetéknéve tartalmazza a 'gen' szót!

select last_name
from sakila.actor
where last_name like "%gen%";

-- 2.c keress meg minden színészt akinek a vezetékneve tartalmazz az `li` szót,
-- és rendezd a találatokat vezetéknév és keresztnév szerint.

select last_name
from sakila.actor
where last_name like "%li%"
order by last_name, first_name;

-- 3. Mennyi különböző vezetéknevű színész van?

select count(distinct last_name) as 'unique actor last_names'
from sakila.actor;

-- 4. Melyik vezeték név szerepel több mint egyszer?

select last_name
from sakila.actor 
group by last_name having count(*) > 1;

-- 5. Jelenítsd meg az összes ország ID-t, és ország nevet, amelyik kína, afganisztán, vagy Izrael!

select country_id,country
from sakila.country
where country in ('China', 'Afghanistan', 'Israel');

-- 6. Mennyi az átlagos hossza egy filmnek?

select avg(length) from sakila.film;

-- 7. Jelenítsd meg az összes személyzet nevét, és címét.

select first_name, last_name, address
from sakila.staff
inner join sakila.address using(address_id);

-- 8. Jelenítsd meg az összes vevő nevét és a fizetett összeget (payment amount).

select first_name, last_name, amount
from sakila.customer
inner join sakila.payment using(customer_id)
limit 10;

-- 9. Jelenítsd meg az összes film címét és a benne szereplő színészek neveit.

select title, first_name, last_name
from sakila.film
inner join sakila.film_actor using(film_id)
inner join sakila.actor using(actor_id)
order by title
limit 20;
