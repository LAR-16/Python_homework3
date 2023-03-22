# Задача 18 поиск ближайшего по значению числа в массиве

number = int(input("Введите количество элементов: "))
find_num = int(input("Введите число,которое будем искать: "))
list_1 = []
for i in range(number):
    elem = 1+i
    list_1.append(elem)
    if i == find_num and find_num != 1 and find_num != list_1[-1]:
        print(f"Ближайшие числа {i-1} и {i+1}")
    elif i == find_num and find_num == 1:
        print(f"Ближайшее число {i+1}")
    elif i+1 == find_num and find_num == number:
        print(f"Ближайшее число {i}")
print(list_1)

if find_num > number:
    print(f"Ближайшее число {list_1[-1]}")
elif find_num < 0:
    print(f"Ближайшее число {list_1[0]}")
