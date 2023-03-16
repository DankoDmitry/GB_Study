use sem1_script;
create table student (id int ,
					  neme varchar (50),
                      phone int,
                      lesson varchar (50));
create table teacher (id int,
					  neme varchar (50),
                      phone int,
                      lesson varchar (50),
                      post varchar (50));
create table course (id int,
				     neme varchar (50));

insert into student values
(1, 'Jon', 12345, 'JS'),
(2, 'Sem', 12346, 'Python');

insert into teacher values
(1, 'Pit', 12345, 'JS', 'prof'),
(2, 'Sem', 12346, 'Python', 'asp');

insert into course values
(1, 'JS'),
(2, 'Python');


select * from student;

select * from teacher;

select * from course;

select neme from student where neme='Jon';

select neme, lesson from student;

select neme from student where neme like 'J%';

insert into student values
(3, 'Tom', 12347, 'JS', 10000),
(4, 'Lock', 12348, 'Python', 5900);

select neme from student where scholarship < 6000;

update student set scholarship = 4000 where id < 3;