# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту,
# орбита которой имеет самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета. 
# Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, 
# зато искусственные спутники были были запущены на круговые орбиты. Результатом функции должен быть кортеж, 
# содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж из пары чисел - 
# полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. 
# При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс в два шага: 
# сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
from math import pi
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# def find_farthest_orbit(orbits):
#     s = [3.14*max(x)*min(x) if max(x) != min(x)
#     else 0 for x in orbits]
#     return(orbits[s.index(max(s))])
# print(find_farthest_orbit(orbits))

def find_farthest_orbit(list_of_orbits):
    list_of_elliptical_orbits = [i for i in list_of_orbits if i[0] != i[1]]
    list_of_areas = [(pi * i[0] * i[1]) for i in list_of_elliptical_orbits]
    max_area_index = list_of_areas.index(max(list_of_areas))
    return list_of_elliptical_orbits[max_area_index]

print(find_farthest_orbit(orbits))