import mehamics as m
import random as r

def make_a_move(player: bool, sweets):

    count = 0

    if player:
        m.output("  ------>   Ход первого игрока.")
    else:
        m.output("  ------>   Ход второго игрока.")

    m.output("На столе {} конфет, сколько хотите взять? ".format(sweets))

    while count > 28 or count < 1 or count > sweets:
        count = int(input("  ------>   "))
        if count > 28 or count < 1:
            m.output("Введите число больше 0 и меньше 29: ")
        elif count > sweets:
            m.output("Нет такого колличества конфет - ещё одна попытка, кожанный мешок: ")
    return count

def make_a_move_with_bot(player: bool, sweets, bot: bool):

    count = 0

    if player and bot:
        m.output("  ------>   Ход бота.")
        
        if sweets >= 28:
            count = r.randint(1, 28)
        else:
            count = r.randint(1, sweets)

        m.output("На столе {} конфет, бот берёт: {}".format(sweets, count))
        
    else:
        m.output("  ------>   Ход игрока.")
        
        m.output("На столе {} конфет, сколько хотите взять? ".format(sweets))
        
        while count > 28 or count < 1 or count > sweets:
            count = int(input("  ------>   "))
            if count > 28 or count < 1:
                m.output("Введите число больше 0 и меньше 29: ")
            elif count > sweets:
                m.output("Нет такого колличества конфет - ещё одна попытка, кожанный мешок: ")
    
    return count

    m.output("На столе {} конфет, сколько хотите взять? ".format(sweets))

def move_first(l):
    if l % 2 == 0: 
        m.output("  ------>   Первым ходит первый игрок: ")
        return True
    else: 
        m.output("  ------>   Первым ходит второй игрок: ")
        return False

