# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
number = input("Введите трёхзначное число: ")
if number.isdigit() == False:
    print('{} это не число'.  format(number)),
    quit()
elif len(number) != 3:
    print('{} не трёзначное число'.  format(number))
    quit()

def sum_numbers(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

sum = sum_numbers(int(number))
print('{} -> {} ({} + {} +{})' .format (number, sum, number[0], number[1], number[2]))