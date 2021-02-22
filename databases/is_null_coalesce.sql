
drop table if exists ecommerce.table1;

create table ecommerce.table1
(id int, name varchar(10), manager varchar(10));

insert into ecommerce.table1 (id, name, manager)
values
(1, null, 'Steve'),
(1, null, null),
(3, 'Matt', 'John'),
(4, 'Raul', null),
(5, 'Peter', 'Sarah');

select * from ecommerce.table1;

select id, ifnull(name, 'name not provided') as name
from ecommerce.table1;

select id, coalesce(name, 'name not provided') as name
from ecommerce.table1;

-- ha van name akkor azt rakja be, ha nincs akkor megnézi hogy van e manager,
-- ha van akkor azt rakja be, ha az sincs akkor a string-et
select id, coalesce(name, manager, 'name not provided') as name
from ecommerce.table1;

select id, coalesce('N/A') as name
from ecommerce.table1;
