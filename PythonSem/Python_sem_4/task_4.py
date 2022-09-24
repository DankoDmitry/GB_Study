import random 

k = random.randint(1, 6)

def equival(l):
    string = ''
    for i in range(l):
        a_i = random.randint(1, 100)
        string += str(a_i) + "*x^" + str(l - i) + " + "
    string += str(random.randint(1, 100)) + ' = 0 \n'
    return string

file = open('C:/Users/ddigo/OneDrive/Рабочий стол/work/GB_Study/PythonSem/Python_sem_4/file.txt', 'w+')
for i in range(random.randint(1, 100)):
    k = random.randint(1, 10)
    file.write(equival(k))
file.close()


file = open('C:/Users/ddigo/OneDrive/Рабочий стол/work/GB_Study/PythonSem/Python_sem_4/file.txt', 'r')
for i in file:
    print(i)
file.close()
