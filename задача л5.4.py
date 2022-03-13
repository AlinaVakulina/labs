#Вакулина Алина - Задание 2 с.р.
import random

n = int(input("Введите количество строк матрицы: "))
m = int(input("Введите количество столбцов матрицы: "))
A = [[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        A[i][j] = random.randint(0, 10)
print("Матрица размера", n, "на", m, ":")
print(A)
print("Строка, в которой находится самая длинная серия одинаковых элементов, имеет номер:")
maxq = 0
q = 0
for i in range(n):
    q = 0
    for j in range(m):
        if (A[i][j]==A[i][j-1]):
            q += 1
        else:
            q = 0
        if(q > maxq):
            maxq = q
for i in range(n):
    q = 0
    for j in range(m):
        if (A[i][j]==A[i][j-1]):
            q += 1
        else:
            q = 0
        if(q == maxq):
             print(i+1, end = ", ")

