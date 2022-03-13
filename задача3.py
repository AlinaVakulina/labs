#Вакулина_задача_3#
a = int(input("Введите длину прямоугольника: "))
b = int(input("Введите ширину прямоугольника: "))
if (a > b):
    max = a
    min = b
else:
    max = b
    min = a
x = max // min
ost = max % min
while (ost != 0):
    max = min
    min = ost
    x = x + (max // min)
    ost = max % min
print("Прямоугольник можно разрезать на", x, "квадратов")
