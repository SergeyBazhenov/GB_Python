# Задача № 19
# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
# на K элементов вправо,  K – положительное число.

# Input:   [1, 2, 3, 4, 5] k = 2

# Output:  [4, 5, 1, 2, 3]
import random

n = int(input('Введите длину списка: '))
k = int(input('Введите число сдвига: '))
l=[]
for num in range(0,n):
    random_number=random.randint(-5,5)
    l.append(random_number)
print(l)

for i in range(k):
    temp = l.pop(-1)
    l.insert(0, temp)

print(l)