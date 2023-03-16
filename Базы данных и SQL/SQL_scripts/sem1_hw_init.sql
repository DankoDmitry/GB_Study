# Создадим БД
CREATE SCHEMA `sem1_hw_mobile_phone` ;

# Подключим БД
use sem1_hw_mobile_phone;

# Создадим таблицу Mobile_phone
create table Mobile_phone (id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
					  ProductName varchar (50),
                      Manufacturer varchar (50),
                      ProductCaunt int,
                      Price int);
                      
# Заполним данными
insert into Mobile_phone 
	(ProductName, Manufacturer, ProductCaunt, Price)
values
	('Galaxy S22 Ultra', 'Samsung', 2, 91575),
	('Galaxy A03 4/64 Gb', 'Samsung', 100, 7451),
	('Galaxy A23 4/64 Gb', 'Samsung', 50, 12395),
	('Galaxy Note20 Ultra 12/256 Gb', 'Samsung', 1, 52196),
	('iPhone 11 128 Gb', 'Apple', 2, 37453),
	('iPhone 12 64 Gb', 'Apple', 15, 46296),
	('iPhone 13 128 Gb', 'Apple', 72, 52544),
	('Redmi Note 10 Pro 6/128 Gb', 'Xiaomi', 23, 17566),
	('Redmi 10 2022 4/64 Gb', 'Xiaomi', 2, 11553),
	('Redmi A1+ 2/32 Gb', 'Xiaomi', 88, 5911);