#Задача_С4.3_Вакулина
import random

n = 10
x = float(input("Введите число: "))
int_array_1 = [0] * n
int_array_2 = []
i = 0
print("10 целочисленных элементов: ")
for i in range(n):
    int_array_1[i] = random.randint(-100,100)
    print(int_array_1[i], end = "; ")
print("\n")
i = 0
for i in range(n):
    if int_array_1[i] >= x:
        int_array_2.append(int_array_1[i])
print("Новый массив, из которого вырезаны элементы, меньше заданной величины:", int_array_2)
