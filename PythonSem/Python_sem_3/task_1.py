import random

# создадим список случайных элементов
list = []
for i in range(random.randrange(1, 10)):
    list.append(random.randrange(1, 10))

# находим сумму элементов на нечётных позициях
S = 0
for i in range(len(list)):
    if i % 2 == 1:
        S += list[i]

print (S, list)