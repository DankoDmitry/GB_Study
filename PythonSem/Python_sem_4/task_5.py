string_1 = str(open("C:/Users/ddigo/OneDrive/Рабочий стол/work/GB_Study/PythonSem/Python_sem_4/task_5_1.txt", 'r').readline())
string_2 = str(open("C:/Users/ddigo/OneDrive/Рабочий стол/work/GB_Study/PythonSem/Python_sem_4/task_5_2.txt", 'r').readline())

list_1 = string_1.replace('*', ' ').split(' ')
list_2 = string_2.replace('*', ' ').split(' ')
list_3 = []

if len(list_1) >= len(list_2):
    for i in range(len(list_1) - len(list_2)):
        list_1.pop(0)
else:
    for i in range(len(list_2) - len(list_1)):
        list_2.pop(0)

for i in range(0, len(list_1)) :
    flag = 1
    try:
        f = int(list_1[i])
    except:
        flag = 0

    # print("flag = %d" % flag)
    # print("list_3 список: ", list_3)

    if flag:
        list_3.append(str(int(list_1[i]) + int(list_2[i])))
    else:
        list_3.append(list_1[i])
        
with open("C:/Users/ddigo/OneDrive/Рабочий стол/work/GB_Study/PythonSem/Python_sem_4/task_5_3.txt", 'w') as f:
    f.write(str(''.join(list_3)))

# a = ['1']
# b = ['2']

# c = ['3']

# c.append(str(int(a[0]) + int(b[0])))

# print(c)

