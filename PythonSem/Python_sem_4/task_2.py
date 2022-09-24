import random
import math

n = random.randrange(1, 1000)

def P(x):
    for i in range(2, int(math.sqrt(x)) + 1): 
        if x % i == 0: return 0
    return 1

list = []

for i in range(2, n // 2 + 1):
    if n % i == 0 and P(i):
        list.append(i)
    
print(n, " -> ", list)
