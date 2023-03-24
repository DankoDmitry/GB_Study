use sem3_hw_work;

CREATE TABLE workers (id INT primary key auto_increment not null,
					Name VARCHAR(45) not null,
					Surname VARCHAR(45) not null,
					Speciality VARCHAR(45) not null,
                    Seniority INT not null,
                    Salary INT not null,
                    Age INT not null);

INSERT INTO workers (Name, Surname, Speciality, Seniority, Salary, Age) VALUES
('Вася','Васькин','начальник',40,100000,60),
('Петя','Петькин','начальник',8,70000,30),
('Катя','Каткина','инженер',2,70000,25),
('Саша','Сашкин','инженер',12,50000,35),
('Иван','Иванов','рабочий',40,30000,59),
('Петр','Петров','рабочий',20,25000,40),
('Сидор','Сидоров','рабочий',10,20000,35),
('Антон','Антонов','рабочий',8,19000,28),
('Юра','Юркин','рабочий',5,15000,25),
('Максим','Воронин','рабочий',2,11000,22),
('Юра','Галкин','рабочий',3,12000,24),
('Люся','Люськина','уборщик',10,10000,49);