import random
class Player:
    def __init__(self):
        self.proffesion = None
        self.reputation = 0
    def set_profession(self,choice):
        if choice == "1":
            self.profession = "Врач"
            self.reputation = 20
            print("-Врач? Отлично, нам очень нужен врач (+20 репутации)")
        elif choice == "2":
            self.profession = "Механик"
            self.reputation = 15
            print ("-Хм, механик значит. Думаю ты можешь нам пригодиться (+15 репутации)")
    def change_reputation(self, amount):
        self.reputation += amount
        if amount >0:
            print(f"Репутация +{amount}, теперь: {self.reputation}")
        elif amount <0:
            print(f"Репутация {amount}, теперь: {self.reputation}")
    def show_status(self):
        print (f"\n[Статус игрока]")
        print (f"Профессия: {self.profession}")
        print (f"Репутация: {self.reputation}/100")



def meet_leader():
    print("""Лидер бункера внимательно смотрит на вас и говорит:
    -Хорошо, ты прошел испытание, но у меня есть для тебя еще одно задание""")
    if player.reputation >= 20:
        print ("Ты уже смог заслужить некоторое уважение. Хочу поручить тебе важное задание.")
    if player.profession == "Врач":
        mission = input ("""
    Выбери задание:
    Осмотреть больных (1)
    Проверить медикаметы (2)
    """)
    elif player.profession == "Механик":
        mission = input ("""
    Выбери задание:
    Починить генератор (1)
    Проверить вентиляцию (2)
    """)
    success = False
    if mission == "1":
        if player.profession == "Врач":
            if player.reputation>= 20:
                print("Благодаря вашей репутации больные вам доверяют")
                print("Вы успешно осмотрели больных и назначили правильно лечение.")
                player.change_reputation(25)
                success = True
            else:
                print("Больные вам не доверяют")
                player.change_reputation(-5)
                success = False
        elif player.profession == "Механик":
            if player.reputation >= 15:
                print("Вы быстро нашли неисправность и успешно починили генератор.")
                player.change_reputation(30)
                success = True
            else:
                print("Вам не хватило опыта для починки генератора")
                player.change_reputation(-10)
                success = False
    elif mission == "2":
        if player.profession == "Врач":
            print("Вы проверили медикаменты и нашли еще запасы")
            player.change_reputation (15)
            success = True
        elif player.profession == "Механик":
            print ("Вы проверили систему вентиляции, все работает.")
            player.change_reputation(10)
            success = True
    return success



print ("3025 год, вы стоите у двери бункера с выжившими")
player = Player()
enter = input("Постучать в дверь (Да/Нет)?")

if "Нет" == enter:
    print ("Вы уходите и погибаете в пустоши")
elif "Да" == enter:
    print ("""Дверь открывает пожилой мужчина и спрашивает:
    - Зачем вы пришли?""")

    enter = input ("""
    Ищу укрытие(1)
    Уже ухожу(2)
    Я пришел ограбить вас (3)
    -""")
    if enter == "2":
        print ("Вы уходите прочь и погибаете в пустоши.")
    elif enter == "3":
        print ("Мужчина выхватывает ружье и убивает вас")
    elif enter == "1":
        print("""Мужчина пропускает вас внутрь и спрашивает:
        - Чем вы можете быть нам полезны?""")
        enter = input ("""
        Я врач(1)
        Я механик(2)
        Я ничего не умею(3)
        -""")
        if enter == "3":
            print ("Мужчина прогоняет вас прочь")
        elif enter == "1" or "2":
            player.set_profession(enter)
            player.show_status()
            print ("""Мужчина предлагает угадать число
        -Я загадал число от 1 до 5, если угадаешь то мы примем тебя, если не угадаешь то придется тебе уйти""")
            import random


            while True:
                secret_number = random.randint(1, 5)
                inp = input("Назовите число: ")
                try:
                    inp = int(inp)
                    if inp == secret_number:
                        print("Ты угадал, проходи")
                        player.change_reputation(10)
                        player.show_status()
                        break

                    else:
                        print(f"Не угадал! Я загадал {secret_number}. Попробуй еще раз.")
                        player.change_reputation(-3)
                        player.show_status()
                except ValueError:
                     print(f"По твоему '{inp}' это число?")
                     player.change_reputation(-5)
                     player.show_status()

            if meet_leader():
                player.show_status()
                print("Поздравляем, теперь вы можете поселиться в бункере!")
                if player.reputation >= 40:
                    print("Ваша репутация позволила вма стать помощником лидера!")
                elif player.reputation >= 25:
                    print ("Вы хорошо поработали и стали уважаемым членом общины.")
                else:
                    print("Придется проделать большую работу, чтобы заслужить уважение членов общины.")
            else:
                player.show_status()
                print("К сожалению вы не справились...")
                if player.reputation <= 0:
                   print("Вас прогоняют прочь.")












