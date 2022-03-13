#Задача_С4.1_Вакулина
import random

n = 10
int_array = [0] * n
i = 0
amax = 0
amin = 0
print("10 целочисленных элементов: ")
for i in range(n):
    int_array[i] = random.randint(-100,100)
    print(int_array[i], end = "; ")
print("\n")
i = 0
while i < len(int_array):
    if int_array[i] < 0:
        if int_array[i] == min(int_array):
            i += 1
            continue
        int_array.pop(i)
        continue
    i += 1
i = 0
for i in range(len(int_array)):
    if int_array[i] == max(int_array):
        amax = i
    if int_array[i] == min(int_array):
        amin = i
d = abs(amax - amin) - 1
print("Количество положительных элементов, располагающихся между максимальным и минимальным элементами -", d)
