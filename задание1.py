#Задание_1_Вакулина
import random

n = int(input("Введите количество элементов массива: "))
array = [0] * n
x = 1
print("Список элементов массива: ")
for i in range(n):
    array[i] = random.randrange(-100,100)
    print(array[i], end = "; ")
print("\n")
i = 0
for i in range(len(array)):
    if i % 2 == 0:
        x = x * array[i]
print("Произведение элементов массива с четными номерами:", x)
