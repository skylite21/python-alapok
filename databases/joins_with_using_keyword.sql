drop table pdo.table1;
drop table pdo.table2;

create table pdo.table1
(id int, value varchar(10));

insert into pdo.table1 (id, value)
values
(1, 'first'),
(2, 'second'),
(3, 'third'),
(4, 'fourth'),
(5, 'fifth');

create table pdo.table2
(id int, value varchar(10));

insert into pdo.table2 (id, value)
values
(1, 'first'),
(2, 'second'),
(3, 'third'),
(6, 'sixth'),
(7, 'seventh'),
(8, 'eighth');

use pdo;
select table1.id as T1ID, table1.value as T1Value,
       table2.id as T2ID, table2.value as T2Value
from table1
inner join table2 on table1.id = table2.id;
    
use pdo;
select table1.id as T1ID, table1.value as T1Value,
       table2.id as T2ID, table2.value as T2Value
from table1
-- egy rövidítése az előző query-nek abban az esetben használható
-- ha az oszlopok neve megegyezik
inner join table2 using(id);


use pdo;
select table1.id as T1ID, table1.value as T1Value,
       table2.id as T2ID, table2.value as T2Value
from table1
inner join table2 on table1.id = table2.id and table1.value = table2.value;

use pdo;
select table1.id as T1ID, table1.value as T1Value,
       table2.id as T2ID, table2.value as T2Value
from table1
-- több oszlop összehasonlítása is működik
-- ha az oszlopok neve megegyezik
inner join table2 using(id, value);
