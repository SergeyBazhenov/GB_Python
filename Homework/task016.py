# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.

# Ввод: 5
# Ввод: 1

# 1 2 1 2 2
# Вывод: 2
import random

# n = int(input("Введите N: "))
# x = int(input("Введите X: "))
# count = 0
# arr = []
# for num in range(0, n):
#     random_number = random.randint(0, x + 10)
#     arr.append(random_number)

# for i in range(len(arr)):
#     if arr[i] == x:
#         count +=1

# print(arr)
# print(count)

#Второй вариант решения задчи, мне не очень нравится.
import random

n = int(input("Введите N: "))
count = 0
arr = []
for num in range(0, n):
    random_number = random.randint(0, 10)
    arr.append(random_number)
print(arr)
x = int(input("Введите X: "))
for i in range(len(arr)):
    if arr[i] == x:
        count +=1
print(count)