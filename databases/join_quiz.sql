drop table pdo.student_class;
drop table pdo.students;
drop table pdo.classes;

create table if not exists pdo.students (
  StudentId int not null auto_increment,
  StudentName varchar(50) not null,
  primary key (StudentId)
  );


create table if not exists pdo.classes (
  ClassId int not null auto_increment,
  ClassName varchar(50) not null,
  primary key (ClassId)
  );

create table if not exists pdo.student_class (
  ClassId int not null,
  StudentId int not null,
  foreign key (ClassId) references pdo.classes(ClassId),
  foreign key (StudentId) references pdo.students(StudentId)
);

insert into pdo.students
(StudentName)
values
('John'),
('Matt'),
('James'),
('Chris');

insert into pdo.classes
(ClassName)
values
('Math'),
('Art'),
('History');


insert into pdo.student_class
(classId, StudentId)
values
(1,1),
(1,2),
(3,1),
(3,2),
(3,3);

select * from pdo.students;
select * from pdo.classes;
select * from pdo.student_class;

-- 1. ki az aki feliratkozott már valamilyen kurzusra?
select DISTINCT pdo.students.StudentName
from pdo.student_class
inner join pdo.students on students.StudentId = student_class.StudentId;

select pdo.classes.ClassName, pdo.students.StudentName
from pdo.student_class
inner join pdo.students on students.StudentId = student_class.StudentId
inner join pdo.classes on classes.ClassId = student_class.ClassId;

-- ki iratkozott fel matekra?
select pdo.students.StudentName
from pdo.student_class
inner join pdo.students on students.StudentId = student_class.StudentId
inner join pdo.classes on classes.ClassId = student_class.ClassId
where className = 'Math';

-- ki az aki nem iratkozott fel semmire?
select StudentName
from pdo.students
left join pdo.student_class on pdo.students.StudentId = pdo.student_class.StudentId
where ClassId is null;

-- mik a fel nem vett tárgyak?
select ClassName
from pdo.classes
left join pdo.student_class on classes.classId = student_class.ClassId
where StudentId is null;
