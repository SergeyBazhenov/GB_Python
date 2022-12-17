# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
n = int(input("Введите число: "))
degree = 0
i = 0
while degree <= n:
    degree = 2**i
    i += 1
  
degree_number = [2**j for j in range(i-1)]
print(degree_number)