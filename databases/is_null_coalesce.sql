drop table if exists pdo.table1;

create table pdo.table1
(id int, name varchar(10), manager varchar(10));

insert into pdo.table1 (id, name, manager)
values
(1, null, 'Steve'),
(2, null, null),
(3, 'third', 'John'),
(4, 'fourth', null),
(5, 'fifth', 'Sarah');


select id, ifnull(name, 'Department name provided') as department_name
from pdo.table1;


select id, coalesce(name, 'department name provided') as department_name
from pdo.table1;


select id, coalesce(name, 'department name provided') as department_name
from pdo.table1;

-- ha a name nem null akkor azt teszi be, ha a manager nem null akkor azt teszi be, ha mindkettő
-- null akkor a stringet
select id, coalesce(name, manager, 'department name provided') as department_name_or_manager
from pdo.table1;

-- a coalesce egy argumentummal is működik, míg az ifnull csak kettővel...
select id, coalesce('N/A') as department_name_or_manager
from pdo.table1;
