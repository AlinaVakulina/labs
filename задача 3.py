#Задача_3_Вакулина#
import math
x = float(input("Введите первую переменную: "))
a = float(input("Введите вторую переменную: "))
num = math.sqrt(math.pi * x) - math.exp(0.2 * math.sqrt(a)) + 2 * math.tan(2 * a) + 1.6 * 10 ** 3 * math.log10(x ** 2)
den = 2 * math.tan(2 * a) * (1/math.cos(x))
print ("Вычисленное y =",round((num/den), 2))
