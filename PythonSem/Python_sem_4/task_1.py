from cmath import pi
import random

b = 10**(-random.randrange(1, 10))
print(f"С точность b = {b}: pi = {pi//b*b}")