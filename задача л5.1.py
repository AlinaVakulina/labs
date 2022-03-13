#Вакулина Алина - Задача Л5.1
import random

n = 5
m = 8
A = [[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
         A[i][j] = random.uniform(-10, 10)
print("Матрица размера 5 на 8: ")
print(A)
min_el = abs(A[0][0])
imin = 1
jmin = 1
for i in range(n):
    for j in range(m):
        if abs(A[i][j]) < min_el:
            min_el = abs(A[i][j])
            imin = i
            jmin = j
print("Минимальный по модулю элемент:", min_el)
print("Координаты элемента:", "[",(imin + 1),";",(jmin + 1),"]")

