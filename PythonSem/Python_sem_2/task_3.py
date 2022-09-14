N = int(input())
mas = []
for i in range(1, N+1):
    c = 1 + (1 / i)
    c **= i
    mas.append(c)
print (mas)