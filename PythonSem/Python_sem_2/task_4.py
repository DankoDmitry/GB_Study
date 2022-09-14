# Создаём запись элементов в positions.txt
with open('positions.txt', 'w') as data:            
    data.write('1 1 1')
    data.close()

# Открываем для чтения файл positions.txt
file = 'positions.txt'
data = open(file, 'r')
for line in data:
    print (line)
    a = list(map(int, line.split()))

# вводим N
N = int(input())

# Вводим массив элементов
arr = [i for i in range(-N, N+1)]

# Переменная для произведения
S = 1

# Произведение
for i in a:
    S *= arr[i]

# Ответ
print (S)