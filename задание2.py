#Задание_2_Вакулина
import random
k = 0
d = 0
n = int(input("Введите количество элементов массива: "))
array = [random.randint(-20, 20) for c in range(n)]
print("Список элементов массива:  ")
for i in range (0,2):
    while k == d:
        k = random.randint(0, n)
    array[k] = 0
    d = k
print(array)
boo = False
for i in range(n):
    if (array[i] == 0) and (boo == False):
        zero1 = i
        boo = True
    elif (array[i] == 0) and (boo == True):
        zero2 = i
s = 0
for i in range(zero1+1, zero2):
    s += array[i] 
print("Сумма элементов массива, расположенных между первым и последним нулевыми значениями:", s)

