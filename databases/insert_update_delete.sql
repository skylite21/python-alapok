
create database if not exists pdo;

-- a tábla és a benne lévő összes érték törlődik:
drop table if exists pdo.actor_sample;

create table if not exists pdo.actor_sample (
  actor_id smallint(5) unsigned not null auto_increment,
  first_name varchar(45) not null,
  last_name varchar(45) null,
  last_update timestamp not null default current_timestamp
    on update current_timestamp,
  primary key (actor_id)
);

-- a tábla összes értékének törlése, de maga a tábla az megmarad:
truncate table pdo.actor_sample;

insert into pdo.actor_sample
(first_name, last_name, last_update)
values
('John', 'Smith', '2013-12-2');

select * from pdo.actor_sample;

-- ha nem definiáljuk az oszlopokat, akkor minden oszlopot definiáli kell,
-- és a megfelelő sorrendben...
insert into pdo.actor_sample
values
(default ,'John', 'Smith', '2013-12-2');

insert into pdo.actor_sample
(first_name, last_name)
values
('John', 'Smith');

insert into pdo.actor_sample
(first_name)
values
('John');

insert into pdo.actor_sample
(last_name)
values
('Smith');

-- select-et használunk az inserttel együtt, egy másik táblából
-- teszünk be adatokat...
insert into pdo.actor_sample
(first_name, last_name)
select first_name, last_name from ecommerce.users
where last_name = 'Lengyel';

-- egyszerre több sor beillesztése:
insert into pdo.actor_sample
(first_name, last_name)
values
('Stan', 'Smith'),
('Hayley', 'Smith'),
('Francine', 'Smith');

update pdo.actor_sample
set first_name = 'David'
where actor_id = 2;

select * from pdo.actor_sample;

-- egyszerre több mező módosítása:
update pdo.actor_sample
set first_name = 'David',last_name = 'Kovács'
where actor_id = 2;

update pdo.actor_sample
set first_name = 'Anonymous'
where actor_id in (2,3,4);

update pdo.actor_sample
set first_name = 'XXX'
where actor_id in (select actor_id from pdo.actor_sample where first_name = 'Anonymous');

delete from pdo.actor_sample
where actor_id = 1;

delete from pdo.actor_sample
where actor_id in (2,3,4);
