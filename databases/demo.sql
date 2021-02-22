

-- mysql parancsokat szokták nagybetűkkel írni...
CREATE DATABASE IF NOT EXISTS ecommerce;
-- nem kötelező a mysql utasításokat nagy betűvel írni:
create database if not exists ecommerce;

create table if not exists ecommerce.rates (
  rental_rate int,
  -- unsigned: csak nem negatív számok lehetnek ennek az oszlopnak az értékei,
  -- ez a pozitív lehetőségetk számát duplázza
  -- auto_increment: minden egyes adatbevitelnél az ID értéke egyel növekszik automatikusan
  -- primary key: egyedi kulcs: az értéke enenk a mezőnek egyedi kell hogy legyen ebben a táblában
  -- nem hozhatok létre két ugyanolyan értékű ID-t.
  id int unsigned auto_increment primary key
);

-- mysql file futatása:  mysql < demo.sql
-- adatbázis megadással:
-- mysql file futatása:  mysql ecommerce < demo.sql
-- adatbázis, felhasználónév és jelszó megadással:
-- mysql file futatása:  mysql -u root -p12345 ecommerce < demo.sql

-- myql adatbázis file-ba kimentése:
-- mysqldump -u root -p12345 ecommerce > dump.sql

insert into ecommerce.rates
-- milyen oszlopokat töltünk fel értékkel:
(rental_rate)
-- mi legyen az érték amit feltöltünk
values
(100);

select * from ecommerce.rates;

create table if not exists ecommerce.users (
  -- varchar: egy adott táblában a varchar típusú mezők hosszának összege nem lehet több mint ~65000
  -- not null: kötelező kitölteni insert-kor
  first_name varchar(50) not null,
  last_name varchar(50) not null,
  user_name varchar(50) not null,
  id int unsigned auto_increment primary key
);

insert into ecommerce.users
(first_name, last_name, user_name)
values
('Lengyel', 'Zsolt', 'Zsolti');

insert into ecommerce.users
(first_name, last_name, user_name)
values
('Kovács', 'János', 'kovi');

select * from ecommerce.users;

-- csak két oszlopot kérünk, first_name szerint rendezve
select first_name, last_name from ecommerce.users
order by first_name desc;


-- SQL : structured query language
select first_name from ecommerce.users
where id > 2;

-- where, és order by együtt is használható
select first_name from ecommerce.users
-- a hasonlítás az itt egy darab egyenlőségjellel van:
where first_name = 'Lengyel'
-- olyat is lehetne hogy first_name > 'Zsolt' és akkor ez után a string után lévőket adja vissza  (abc szerint...)
order by last_name desc;

-- empty result set:
select first_name from ecommerce.users
-- nem egyenlő: vagy != vagy így jelölik: <>
where 1 = 2;


select first_name as `Keresztnév`
from ecommerce.users;

create table if not exists ecommerce.movies (
  duration int,
  id int unsigned auto_increment primary key
);

select duration/60 as TimeInHour
from ecommerce.movies;


select rental_rate * 1.27 as `bruttó ár` from ecommerce.rates;

select (cast(rental_rate as float) * 1.27) / 2 as `float típus` from ecommerce.rates;

-- lekérdezi a tábla mezőinek nevét és tulajdonságait:
describe ecommerce.rates;

create table if not exists ecommerce.payment(
  amount int,
  -- van külön date, és time típus is...
  created datetime,
  id int unsigned auto_increment primary key
);

insert into ecommerce.payment (amount, created) values (123, '2020-01-18-15-16');
insert into ecommerce.payment (amount, created) values (312, curdate());
insert into ecommerce.payment (amount, created) values (312, now());

select round(amount) from ecommerce.payment;

select concat(first_name, ' ', last_name) as FullName from ecommerce.users;

select concat(left(first_name, 1), ' ', left(last_name, 1)) as Monogramm
from ecommerce.users;

select * from ecommerce.payment;

-- https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_date-format
select date_format(created, '%Y %b, %d - %T : %f ') as TheDate from ecommerce.payment;

select amount from ecommerce.payment
  where created between '2020-01-01' and '2020-12-12 12:59:59';

select amount from ecommerce.payment
  where created between '2020-01-01' and now();

select created, 
  weekday(created) +1 as dayofweek,
  quarter(created) as quarter,
  week(created) as weekoftheyear,
  monthname(created) as monthname
  from ecommerce.payment;

select * from ecommerce.rates;
-- csak az egyedi értékeket adja vissza
select DISTINCT rental_rate from ecommerce.rates;
-- hány egyedi értéke van a rental_rate-nek:
select count(DISTINCT rental_rate) from ecommerce.rates;
-- összesen hány érték van a táblában:
select count(rental_rate) from ecommerce.rates;

-- A logikai operátorok működnek, de ha a sorrendet meg akarjuk szabni akkor használjunk
-- zárójeleket!!!
select * from ecommerce.rates
-- https://dev.mysql.com/doc/refman/8.0/en/operator-precedence.html
  where rental_rate = 100 and (id < 5 or id > 20);

-- Ha kiváncsi vagy a tábla oszlopaira és azok típusaira
describe ecommerce.users;

insert into ecommerce.users
(first_name, last_name, user_name)
values ('Zsolt', 'Lengyel', 'skylite');

select * from ecommerce.users;

insert into ecommerce.users
(first_name, last_name, user_name)
values ('István', 'Kovács', 'pityu'),
('Gábor', 'Benke', 'Gabesz'),
('Nóra', 'Király', 'Noncsi');

select *
from ecommerce.users
where first_name in ('Gábor', 'Nóra');

select *
from ecommerce.users
where first_name not in ('Gábor', 'Nóra');

select customerName
from classicmodels.customers
where customerNumber between 300 and 310;

select customerName
from classicmodels.customers
where customerName like 'al%';

select customerName
from classicmodels.customers
where customerName like '%' order by customerName;

select customerName
from classicmodels.customers
where customerName like 'b_a%';

select customerName
from classicmodels.customers
where customerName like 'b%a%';

select *
from classicmodels.offices;

select *
from classicmodels.offices
where state is null;

select *
from classicmodels.products
order by productVendor, productLine desc;

select user_name, concat(first_name, ' ',last_name) as full_name
from ecommerce.users
order by concat(first_name, ' ', last_name);

select user_name, concat(first_name, ' ',last_name) as full_name
from ecommerce.users
order by full_name;


-- limit: limitálja a visszaadott sorok számát
select *
from classicmodels.payments
order by customerNumber
limit 10;

-- a limitnek ha kettő paramétert adunk akkor az első paraméter az hogy honnan kezdje
select *
from classicmodels.payments
order by customerNumber
limit 10, 2;

-- a 6odik még nem lesz benne, a kettő pedig az a kettő amelyik a 6odik után jön
select *
from ecommerce.users
limit 6, 2;

-- <>	 Not equal to-t igy is jelolik vagy siman !=
