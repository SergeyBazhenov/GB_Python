# Задач № 23
# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента с
# предыдущим номером)


# Input: [0, -1, 5, 2, 3]
# Output: 2

# пояснение
# (-1 < 5, 2 < 3)
import os
os.system('cls')

import random

n = int(input("Введите длину списка: "))

l = []
for num in range(0, n):
    random_number = random.randint(-5, 5)
    l.append(random_number)
print(l)
count = 0
for i in range(1, len(l)):
    if l[i - 1] < l[i]:
        count += 1
print(count)
