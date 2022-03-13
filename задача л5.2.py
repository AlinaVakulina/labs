#Вакулина Алина - Задача Л5.2
import numpy as np
import random

n = 6
m = 9
A = np.random.randint(-10, 10, size=(n, m))
A[random.randint(0, n-1)][random.randint(0, m-1)] = 0
print("Матрица размера 6 на 9: ")
print(A)
print("Столбец Номер элемента")
no_nul = True
for j in range(m):
    no_nul = True
    for i in range(0, n):
            if (A[i][j] == 0):
                no_nul = False
                print(" ", (j+1), "        ", (i+1))
    if no_nul == True:
        print(" ", j+1, "    ", "Нулей нет")


