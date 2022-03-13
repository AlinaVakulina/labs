#Вакулина Алина - Задача 1 с.р.
import random

def name(n, m):
    A = [[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            A[i][j] = random.randint(-10, 10)
    A [random.randint(0, n-1)][random.randint(0, m-1)] = 0
    print("Матрица размера", n, "на", m, ":")
    print(A)
    t = 0
    s = 0
    for j in range(m):
        for i in range(n):
            if A[i][j] != 0:
                t += 1
        if t == n:
            s += 1
        t = 0
    result = m - s                              
    return result
n = int(input("Введите количество строк матрицы: "))
m = int(input("Введите количество столбцов матрицы: "))
result = name(n, m)
print("Количество столбцов, содержащих хотя бы один нулевой элемент:", result)

