use sem3_hw_work;
/*
+ Таблица для работы на слайде.
+ Отсортируйте поле “зарплата” (salary) в порядке убывания
+ Отсортируйте поле “зарплата” (salary) в порядке возрастания
+ Выведите 5 максимальных зарплат (salary)
+ Подсчитать суммарную зарплату(salary) по каждой специальности (speciality)
+ Найти количество сотрудников по специальности “Рабочий” (speciality) в возрасте от 24 до 42 лет.
+ Найти количество специальностей
+ Вывести специальности, у которых средний возраст сотрудника меньше 44 лет
*/

SELECT * FROM workers ORDER BY Salary DESC;
SELECT * FROM workers ORDER BY Salary ASC;

SELECT Salary FROM workers ORDER BY Salary DESC LIMIT 5;

SELECT Speciality, SUM(Salary) AS Summ FROM workers GROUP BY Speciality;

SELECT COUNT(*) AS 'Count' FROM workers WHERE Speciality = 'Рабочий' GROUP BY Speciality;

SELECT COUNT(distinct Speciality) AS 'Count' FROM workers;

SELECT Speciality FROM  workers GROUP BY Speciality HAVING AVG(Age) < 44;

