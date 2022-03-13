#Задача_4_1_Вакулина#
import math
a = float(input("Введите переменную (угол в численных единицах): "))
z1 = float(math.sin(2 * a) + math.sin(5 * a) - math.sin(3 * a))/(math.cos(a) + 1 - 2 * (math.sin(2* a) ** 2))
print ("Вычисленное z1 =", z1)
