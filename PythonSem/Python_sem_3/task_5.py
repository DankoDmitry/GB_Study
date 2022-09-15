import random

# создадим случайный элемент
N = random.randint(0, 40)

print (N)

def F(n):
    if n == -1 or n == 1 or n == 2: return 1
    elif n == -2: return -1
    elif n == 0: return 0
    elif n > 2: return int(F(n-1) + F(n-2))
    elif n < -2: return int(F(n+2) - F(n+1))

list = [F(i) for i in range(-N, N + 1)]
print (list)
