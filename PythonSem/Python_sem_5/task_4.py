import random

# создадим случайный элемент
N = random.randint(0, 100)

# создадим его копию и строку для преобразования
n = N
nomder_in_bin = ''

# преобразуем
while N > 0:
    if N % 2 == 0:
        nomder_in_bin = '0' + nomder_in_bin
    else:
        nomder_in_bin = '1' + nomder_in_bin
    N //= 2

# исправим исключение
if nomder_in_bin == '': nomder_in_bin = '0'    

nomder_in_bin = int(nomder_in_bin)

print ('{} -> {}'.format(n, nomder_in_bin))