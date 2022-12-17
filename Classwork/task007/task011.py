# Задача №11
# Дано натуральное число A > 1. 
# Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.

def fibonache(n):
    # 0 1 1 2 3 5 8 

    if n == 0:
        return 1
    if n == 1:
        return 2 
    number0 = 0
    number1 = 1
    count = 2
    while n >= number1:
        if n == number1:
            return count
        temp = number1
        number1 += number0
        number0 = temp
        count += 1
    return -1

n = int(input('Введите число: '))
print(fibonache(n))