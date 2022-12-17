# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
import math

while True:
    try:
        sum = int(input("Введите число меньше или равное 1000: "))
        p = int(input("Введите число меньше или равное 1000: "))
        if sum > 1000 or p > 1000:
            print("Одно из введеных чисел больше 1000")
            break
        elif p == 0:
            print(f"{sum} и 0")
            break
        else:
            D = sum**2 - 4 * p

            if D < 0:
                print("Решения нет!")
                break
            else:
                x = (sum + math.sqrt(D)) / 2

                if int(x) == x:
                    y = sum - x
                    print(int(x), "и", int(y))
                    break
                else:
                    print("Решения нет!")
                    break

    except:
        print("Вы ввели что-то не то, попробуте ещё раз.")