use sem2_hw_salees;
/*
Используя операторы языка SQL, создайте табличку “sales”. Заполните ее данными
Сгруппируйте значений количества в 3 сегмента — меньше 100, 100-300 и больше 300.
Создайте таблицу “orders”, заполните ее значениями. Покажите “полный” статус заказа, используя оператор CASE
Чем NULL отличается от 0?
*/

CREATE TABLE sales (id INT primary key auto_increment not null,
					order_date DATE not null,
                    amount INT not null);
                    
INSERT INTO sales (order_date, amount)
VALUES
  ("2021-10-26",285),
  ("2022-11-15",150),
  ("2023-03-19",283),
  ("2022-08-12",310),
  ("2023-05-03",141),
  ("2023-08-28",149),
  ("2023-02-02",105),
  ("2022-09-27",315),
  ("2022-03-10",209),
  ("2023-09-11",176),
  ("2022-03-28",291),
  ("2022-09-28",212),
  ("2022-06-29",122);
  
SELECT id, order_date, amount,
CASE TRUE
    WHEN amount < 100 THEN 'меньше 100'
    WHEN amount >= 100 AND amount <= 300 THEN '100-300'
    ELSE 'больше 300'
END AS order_size
FROM sales;

CREATE TABLE orders (
    orderid INT primary key auto_increment not null,
    employeeid VARCHAR(5) not null,
    amount DECIMAL(20, 2) not null,
    orderstatus VARCHAR(45) not null
);

INSERT INTO orders (employeeid, amount, orderstatus)
VALUES
("e03",50.65,"OPEN"),
("e02",33.34,"OPEN"),
("e03",7.90,"CLOSED"),
("e03",58.30,"CLOSED"),
("e03",15.02,"CANCELLED"),
("e05",28.46,"CLOSED"),
("e04",23.70,"OPEN"),
("e02",84.01,"OPEN"),
("e06",29.08,"OPEN"),
("e07",23.53,"OPEN"),
("e03",58.08,"CLOSED"),
("e03",58.88,"OPEN");

SELECT orderid, orderstatus,
CASE orderstatus
    WHEN "OPEN" THEN 'Order is in open state.'
    WHEN "CLOSED" THEN 'Order is closed.'
    ELSE 'Order is cancelled.'
END AS order_summary
FROM orders;