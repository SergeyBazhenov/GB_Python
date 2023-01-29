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

n = '10 * 10 * 10'#"22 * 300 - 14 + 10 * 10 + 10 * 10"

m = n.split()
m2 = []

print(m)


def calc(a, b, ch):
    if ch == "+":
        return a + b
    elif ch == "-":
        return a - b
    elif ch == "/":
        return a / b
    elif ch == "*":
        return a * b


# a = int(m[0])
# c = m[1]
# b = int(m[2])

result = int(m[0])

for i in range(1, len(m) - 1, 2):
    if m[i] == "*" or m[i] == "/":
        result = calc(int(m[i - 1]), int(m[i + 1]), m[i])
        m.append(result)
                
    else:
        m.append(m[i])
        m.append(int(m[i + 1]))


print(m[i], m[i + 1])
print(m)
print(result)
