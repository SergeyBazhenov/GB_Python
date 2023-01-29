# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Начинайте с 200 конфет и более!
import random

def bot_calc(value):
    if value > 114:
        k = random.randint(1,29)
    elif value >= 86:
        k = value - 85
    elif value >= 59:
        k = value - 58
    else:
        k = value - 29
    return k
 
player1 = input("What is your name?: ")
player2 = "Bot"
value = int(input("How many sweets will be on the table?: "))
flag = random.randint(0, 2)
if flag:
    print(f"{player1} get ready!")
else:
    print(f"{player2} get ready!")
 
counter1 = 0
counter2 = 0
 
while value > 28:
    if flag:
        k = input_sweets(player1)
        counter1 += k
        value -= k
        flag = False
        print_way(player1, k, counter1, value)
    else:
        k = bot_calc(value)
        counter2 += k
        value -= k
        flag = True
        print_way(player2, k, counter2, value)
 
if flag:
    print(f" {player1} поздравляю! Ты сделал это и победил Конфетного Бота")
else:
    print(f" Ты проиграл:( {player2} забирает последнюю конфету и выигрывает!")