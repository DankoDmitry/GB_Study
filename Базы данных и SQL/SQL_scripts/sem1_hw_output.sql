# Подключим БД
use sem1_hw_mobile_phone;

# Проверим, что БД заполнена
select * from Mobile_phone;

# Задание 2: Выведите название, производителя и цену для товаров, количество которых превышает 2 (SQL - файл, скриншот, либо сам код)
select ProductName, Manufacturer, Price from Mobile_phone where ProductCaunt > 2;

# Задание 3: Выведите весь ассортимент товаров марки “Samsung”
select ProductName from Mobile_phone where Manufacturer='Samsung';

# Задание 4: Выведите информацию о телефонах, где суммарный чек больше 100 000 и меньше 145 000**
select * from Mobile_phone where ProductCaunt*Price > 100000 and ProductCaunt*Price < 145000;

# Задания 5:
# 5.1. Товары, в которых есть упоминание "Iphone"
select ProductName from Mobile_phone where ProductName like '%Iphone%';

# 5.2. "Galaxy"
select ProductName from Mobile_phone where ProductName like '%Galaxy%';

# 5.3.  Товары, в которых есть ЦИФРЫ
select ProductName from Mobile_phone where ProductName NOT LIKE '%[^0-9]%';

# 5.4.  Товары, в которых есть ЦИФРА "8"  
select ProductName from Mobile_phone where ProductName LIKE '%8%';
