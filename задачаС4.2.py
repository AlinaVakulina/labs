#Задача_С4.2_Вакулина
import random

n = int(input("Введите количество элементов массива: "))
float_array = [0] * n
i = 0
s = 0
neg = 0
print("Список элементов массива: ")
for i in range(len(float_array)):
    float_array[i] = random.uniform(-100,100)
    print(float_array[i], end = "; ")
    if float_array[i] < 0:
        neg = i
print("\n")
i = 0
for i in range(len(float_array)):
    if i > neg:
        s += float_array[i]
print("Сумма элементов, расположенных правее последнего отрицательного элемента массива:", round(s, 2))
