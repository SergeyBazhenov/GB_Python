# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся.
# Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32
first = int(input("Первый класс >>> "))
sec = int(input("Второй класс >>> "))
thrd = int(input("Третийй класс >>> "))
first_klass = (first + 1) // 2
sec_klass = (sec + 1) // 2
thrd_klass = (thrd + 1) // 2
sum = first_klass + sec_klass + thrd_klass

print(first_klass)
print(sec_klass)
print(thrd_klass)
print(sum)
