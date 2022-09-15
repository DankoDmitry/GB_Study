import random

# создадим список случайных элементов
list = []
for i in range(random.randrange(1, 10)):
    list.append(random.randrange(1, 10))

# находим сумму элементов на нечётных позициях
new_list = []
if len(list)%2 == 0:
    N = len(list) // 2
else:
    N = len(list) // 2 + 1
for i in range(N):
    new_list.append(list[i]*list[-i - 1])

print ("{} => {}".format(list, new_list))