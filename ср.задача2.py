#Вакулина_СР_Задача_2#
xA = float(input("Введите абсциссу точки A, образующей треугольник ABC, xA = "))
yA = float(input("Введите ординату точки A, образующей треугольник ABC, yA = "))
xB = float(input("Введите абсциссу точки B, образующей треугольник ABC, xB = "))
yB = float(input("Введите ординату точки B, образующей треугольник ABC, yB = "))
xC = float(input("Введите абсциссу точки C, образующей треугольник ABC, xC = "))
yC = float(input("Введите ординату точки C, образующей треугольник ABC, yC = "))
xN = float(input("Введите абсциссу произвольной точки N, xN = "))
yN = float(input("Введите ординату произвольной точки N, yN = "))
AB = ((xB - xA) ** 2 + (yB - yA) ** 2) ** (1/2)
BC = ((xC - xB) ** 2 + (yC - yB) ** 2) ** (1/2)
AC = ((xC - xA) ** 2 + (yC - yA) ** 2) ** (1/2)
AN = ((xN - xA) ** 2 + (yN - yA) ** 2) ** (1/2)
BN = ((xN - xB) ** 2 + (yN - yB) ** 2) ** (1/2)
CN = ((xN - xC) ** 2 + (yN - yC) ** 2) ** (1/2)
pABC = (AB + BC + AC) / 2
pABN = (AB + BN + AN) / 2
pACN = (AC + CN + AN) / 2
pCBN = (BC + BN + CN) / 2
SABC = (pABC * (pABC - AB) * (pABC - BC) * (pABC - AC)) ** (1/2)
SABN = (pABN * (pABN - AB) * (pABN - BN) * (pABN - AN)) ** (1/2)
SACN = (pACN * (pACN - AC) * (pACN - CN) * (pACN - AN)) ** (1/2)
SCBN = (pCBN * (pCBN - BC) * (pCBN - BN) * (pCBN - CN)) ** (1/2)
if ((SABN + SACN + SCBN)<= SABC):
    print("Точка N находится внутри треугольника ABC")
else:
    print("Точка N находится вне треугольника ABC")
