#Вакулина_задача_2#
import math
e = 0.0001
l = float(input("Введите левую границу: "))
r = float(input("Введите правую границу: "))
x = (r + 1) / 2
n = 0
while abs(r - l) > e:
    n = n + 1
    if (((math.cos(x) - x) * (math.cos(l) - l)) < 0):
        r = x
    else:
        l = x
    x = (r + l) / 2
    if n >= 500:
        exit()
print("Корень уравнения x =", x)
print("Количество итераций n =", n)
    
