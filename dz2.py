#n = int(input("Введите целое число N:"))
#sum = 1
#for i in range(1,n):
#    sum = sum + i
#    print("Сумма чисел от 1 до", n, "равна", sum)

import random

#N = random.randint(1, 100)
#i = input("Угадайте число:")
#i = int(i)
#if i > N:
#    print ("Ваше число больше")
#if i < N:
    #print ("Ваше число меньше")
#if i == N:
   # print ("Ура, угадал!")


while True:
    inp = input('Введите целое число:')

    try:
        inp = int(inp)

        ret = inp ** 3
        print(f'Куб введенного числа равен {ret}')
    except:
        print(f'Нужно целое число, а вы ввели: {inp}')
    finally:
        print("Попробуйте еще раз!")


