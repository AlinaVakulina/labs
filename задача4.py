#Вакулина_задача_4#
a = 1
print("Все пифагоровы числа, не превышающие 15:")
for a in range(a, 16):
    for b in range (a, 16):
        for c in range (b, 16):
            if a ** 2 + b ** 2 == c ** 2:
                print(a, b, c)
