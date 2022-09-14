import random

list = ['1','2','3','4','5','6','7','8','9','10','11','12','13']

print (list)
new_list = []

while list != []:
    new_list.append(list.pop(random.randrange(0, len(list))))

print (new_list)
