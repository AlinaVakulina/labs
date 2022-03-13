#Задание_3_Вакулина
import random

n = int(input("Введите количество элементов массива: "))
array = [0] * n
array1 = []
array2 = []
i = 0
print("Список элементов массива: ")
for i in range(n):
    array[i] = random.randrange(-100,100)
    print(array[i], end = "; ")
print("\n")
i = 0
for i in range(n):
    if array[i] >= 0:
        array1.append(array[i])
    else:
        array2.append(array[i])
array1.extend(array2)
print("Упорядоченный массив:", array1)
