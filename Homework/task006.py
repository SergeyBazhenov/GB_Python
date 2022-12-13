# Задача 6
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд 
# и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no
number = input("Введите номер билета: ")
if number.isdigit() == False:
    print('{} - это не номер билета'.  format(number)),
    quit()
elif len(number) != 6:
    print('{} Вы ввели неверный номер билета'.  format(number))
    quit()
first = number[0:3]
second = number[3:6]

def sum_numbers(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

first_sum = sum_numbers(int(first))
second_sum = sum_numbers(int(second))

if first_sum == second_sum:
    print('{} -> yes' .format (number))
else:
    print('{} -> no' .format (number))

