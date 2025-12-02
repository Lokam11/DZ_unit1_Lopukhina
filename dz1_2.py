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
    mission = input ("""
    Выбери задание:
    Починить генератор(1)
    Осмотреть тоннель(2)
    """)
    if mission == "1":
        print("Вы успешно починили генератор, теперь в бункере есть электричество!")
        return True
    elif mission == "2":
        print("В тоннеле вы нашли запасы еды и лекарств, отличная работа!")
        return True
    else:
        print("Вы не смогли выбрать задание и вас выгнали.")
        return False
print ("3025 год, вы стоите у двери бункера с выжившими")
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
                        if meet_leader():
                            print("Поздравляем, теперь вы можете поселиться в бункере!")
                        else:
                            print("К сожалению вы не справились.")
                        break
                    else:
                        print(f"Не угадал! Я загадал {secret_number}. Попробуй еще раз.")
                except ValueError:
                     print(f"По твоему '{inp}' это число?")










