#Вакулина_задача_1#
import math
Max = 500
x = float(input("Введите аргумент: "))
e = float(input("Введите точность: "))
sinx = math.sin(x)
c = x
y = c
n = 1
while abs(c) > e:
    c = -c * x ** 2 / (2 * n * (2 * n + 1))
    y = y + c
    n = n + 1
    if n > Max:
        print("Ряд расходится!")
        exit()
print("Аргумент: ", x,"\n",
      "Значение функции: ", y,"\n",
      "Вычислено с точностью:", e, "за", n, "итераций","\n",
      "Значение функции, вычисленное с помощью стандартной функции sin(x): ", sinx)
