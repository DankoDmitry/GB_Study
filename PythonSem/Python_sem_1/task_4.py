mas = ['(0, +"бесконечность")', '(0, -"бесконечность")']
const = int(input('Введите номер четверти: '))
if (const == 1):
    print("X = {}, Y = {}".format(mas[0], mas[0]))
elif (const == 2):
    print("X = {}, Y = {}".format(mas[1], mas[0]))
elif (const == 3):
    print("X = {}, Y = {}".format(mas[1], mas[1]))
elif (const == 4):
    print("X = {}, Y = {}".format(mas[0], mas[1]))
else:
    print("Нет накой четверти")