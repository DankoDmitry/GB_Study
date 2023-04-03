use sem4_hw;
/*
Используя JOIN-ы, выполните следующие операции:
Вывести всех котиков по магазинам по id (условие соединения shops.id = cats.shops_id)
Вывести магазин, в котором продается кот “Мурзик” (попробуйте выполнить 2 способами)
Вывести магазины, в которых НЕ продаются коты “Мурзик” и “Zuza”
*/

SELECT name, shopname FROM cats
LEFT OUTER JOIN shops
ON shops.id = cats.shops_id;

SELECT name, shopname FROM cats
LEFT OUTER JOIN shops
ON shops.id = cats.shops_id
WHERE cats.name = "Murzik";

# или

SELECT name, shopname FROM shops
RIGHT OUTER JOIN cats
ON shops.id = cats.shops_id
WHERE cats.name = "Murzik";

SELECT name, shopname FROM cats
LEFT OUTER JOIN shops
ON shops.id = cats.shops_id
WHERE cats.name != "Murzik" AND cats.name != "Zuza";

/*
Вывести название и цену для всех анализов, которые продавались 5 февраля 2020 и всю следующую неделю.
Есть таблица анализов Analysis:
	an_id — ID анализа;
	an_name — название анализа;
	an_cost — себестоимость анализа;
	an_price — розничная цена анализа;
	an_group — группа анализов.
Есть таблица групп анализов GroupsAn:
	gr_id — ID группы;
	gr_name — название группы;
	gr_temp — температурный режим хранения.
Есть таблица заказов Orders:
	ord_id — ID заказа;
	ord_datetime — дата и время заказа;
	ord_an — ID анализа.
*/

SELECT an_name, an_price FROM Analysis
LEFT OUTER JOIN Orders
ON Analysis.an_id = Orders.ord_an
WHERE Orders.ord_datetime > '2020-02-05 00:00:0' AND Orders.ord_datetime < '2020-02-13 00:00:00';

