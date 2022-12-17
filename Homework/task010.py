# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2
import random


def coins(N):
    coin = []
    for _ in range(N):
        coin.append(random.randint(0, 1))
    print(coin)
    count_0 = 0
    count_1 = 0

    for item in range(N):
        if coin[item] == 1:
            count_1 += 1            
        else:
            count_0 += 1
            
    if count_0 < count_1:
        return count_0
    else:
        return count_1


# if count_0 > count_1:
#     print(count_0)
# else:
#     print(count_1)

n = int(input("Введите количество монет: "))

print(f"Нужно перевернуть {coins(n)} монет.")
