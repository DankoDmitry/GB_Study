import random

# создадим список случайных элементов
list = []
for i in range(random.randrange(1, 10)):
    list.append(random.uniform(1, 10))
print (list)

# уберём целую часть
for i in range(len(list)):
    list[i] = list[i] % 1

print (list)

# найдём разницу
max = list[0]
min = list[0]
for i in range(len(list)):
    if (min > list[i]):
        min = list[i]
    if (max < list[i]):
        max = list[i]

print ('{} => {}'.format(list, max - min))