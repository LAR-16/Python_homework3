# Задача 16 сколько раз элемент встречается в массиве
from random import randint
number = int(input("Введите количество элементов: "))
find_num = int(input("Введите число,которое будем искать: "))
list_1 = []
count = 0
for i in range(number):
    elem = randint(1, number)
    list_1.append(elem)
    if list_1[i] == find_num:
        count += 1
print(list_1)
print(f"Искомое число встречается {count} раз")
