# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.

# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6
import random

n = int(input("Введите число N: "))
array = []
for num in range(n):
    random_number = round(random.randint(1, n))
    array.append(random_number)

print(array)
x = int(input("Введите число X: "))


def find_num(count):

    for i in range(0, len(array)):
        if array[i] == x - count:
            return array[i]
        elif array[i] == x + count:
            return array[i]

    return find_num(count + 1)


print(find_num(0))