import random as rd

legth = rd.randrange(10, 100)
list = []

for i in range(legth):
    list.append(rd.randrange(1, 30))

new_list = []

for i in list:
    if i not in new_list:
        new_list.append(i)

print("Исходный список: ", list)
print("Итоговый список: ", new_list)