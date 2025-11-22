#n = int(input("Введите целое число N:"))
#sum = 1
#for i in range(1,n):
#    sum = sum + i
#    print("Сумма чисел от 1 до", n, "равна", sum)

import random

N = random.randint(1, 100)
i = input("Угадайте число:")
i = int(i)
if i > N:
    print ("Ваше число больше")
if i < N:
    print ("Ваше число меньше")
if i == N:
    print ("Ура, угадал")


