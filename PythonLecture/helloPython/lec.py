with open ('file.txt', 'w') as data:
    data.write('1 2 3 4 5 6 7 8 9')
    data.close()

with open ('file.txt', 'r') as data:
    l = list(data.readlines())
    data.close()

print (l)
print (type(l))

l.split()
print (l)