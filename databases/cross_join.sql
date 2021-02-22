drop table if exists pdo.table1;
drop table if exists pdo.table2;

create table pdo.table1
(id int, value varchar(10));

create table pdo.table2
(id int, value varchar(10));

insert into pdo.table1 (id, value)
values
(1, 'first'),
(2, 'second'),
(3, 'third'),
(4, 'fourth'),
(5, 'fifth');

insert into pdo.table2 (id, value)
values
(1, 'first'),
(2, 'second'),
(3, 'third'),
(6, 'sixth'),
(7, 'seventh'),
(8, 'eighth');


-- cross join: mindent mindennel joinol
select pdo.table1.*, pdo.table2.*
from pdo.table1
cross join pdo.table2;

-- ha nem adunk meg feltételt akkor a cross join az alapértelmezett join ez 
-- viszont nem segiti az olvashatóságot
select pdo.table1.*, pdo.table2.*
from pdo.table1
join pdo.table2;

