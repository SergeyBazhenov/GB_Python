# Вычислить значение выражения:
# 12 + 15
# 12 / 15
# 112 * 15


# 1. Где операторы?
# 2. Где числовые значения?


# Уровень 1:

# - 1 действие
# - 2 аргумента

# Уровень 2:

# - Количество действие произвольное
# 12 + 15 - 4


# Уровень 3:
# - Действия имеют приоритет

# 12 - 4*2

# Уровень 4:
# - Действия разделяются скобками

# (12 - 4) * 2

# 1 действие
# n = '22 + 300'
# m = n.split()

# a = int(m[0])
# c = m[1]
# b = int(m[2])
# print(a, b, c)

# if c == '+':
#     print(a + b)
# elif c == '-':
#     print(a - b)
# elif c == '/':
#     print(a / b)
# elif c == '*':
#     print(a * b)

# 2 действие

import os

os.system('cls')

def calc(a, b, ch):
    if ch == '+':
        return a + b
    elif ch == '-':
        return a - b
    elif ch == '/':
        return a / b
    elif ch == '*':
        return a * b


n = '10 * 10 * 10 / 22 * 300 - 14 + 10 * 10 + 10 * 10'
input_list = n.split()

first_prior = '()'
second_prior = '*/'
third_prior = '+-'

rpn = []
stack = [n[1]]

for i in range(len(input_list)):
    if input_list[i].isdigit():
        rpn.append(input_list[i])

    elif input_list[i] in third_prior: 
        while stack[-1] in third_prior or stack[-1] in second_prior:
            rpn.append(stack[-1])
            stack.pop()    
        stack.append(input_list[i])

    elif input_list[i] in second_prior:
        if stack[-1] in second_prior:
            rpn.append(stack[-1])
            stack.pop()
        stack.append(input_list[i])

    elif input_list[i] == '(':
        stack.append(input_list[i])

    elif input_list[i] == ')':
        rpn.append(stack[-1])
        while stack[-1] != '(':
            stack.pop()
        stack.pop()       
        
    

stack.reverse()
stack.pop()

rpn += stack

result_list = []

for i in range(len(rpn)):
    
    if rpn[i] in '+-*/':
        b = float(result_list.pop())
        a = float(result_list.pop())
        result_list.append(calc(a, b, rpn[i]))
    
    else:
        result_list.append(rpn[i])
   

print(f'Результат равен: {result_list[0]}')