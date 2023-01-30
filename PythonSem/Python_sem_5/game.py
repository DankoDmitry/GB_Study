import random as r
import player as p
import mehamics as m



def game_with_friend():
    
    sweets = 20
    scort_true = 0
    scort_false = 0


    player = p.move_first(r.randint(0, 2))

    while sweets > 0:

        counter = p.make_a_move(player, sweets)

        if player:
            scort_true += counter
            sweets -= counter
        else:
            scort_false += counter
            sweets -= counter
    
        player = not player

    m.win_game(not player)

def game_with_bot():

    sweets = 20
    scort_true = 0
    scort_false = 0

    player = p.move_first(r.randint(0, 2))

    bot = not player

    while sweets > 0:

        counter = p.make_a_move_with_bot(player, sweets, bot)

        if player:
            scort_true += counter
            sweets -= counter
        else:
            scort_false += counter
            sweets -= counter
    
        player = not player

    m.win_game_with_bot(not player, bot)