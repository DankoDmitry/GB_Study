
def output(data):
    print(data)

def win_game(player: bool):
    if player:
        output("  ------>   Первый игрок выиграл игру! Ура!!!")
    else:
        output("  ------>   Второй игрок выиграл игру! Ура!!!")


def win_game_with_bot(player: bool, bot: bool):
    if player and bot:
        output("  ------>   Бот выиграл игру! Следующим, бот захватит мир!!!")
    else:
        output("  ------>   Игрок выиграл игру! Ура!!!")