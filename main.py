import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 0
        self.alive = True

    def to_study(self):
        print("Тре зубрити")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("Хочу дрихнути")
        self.gladness += 3

    def to_work(self):
        print("Я камєнщік работаю трі дня бєз зарплати")
        self.money += 115

    def to_chill(self):
        print("Пішов прокрастинувати")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 75

    def is_alive(self):
        if self.progress < -0.5:
            print("Press F...")
            self.alive = False
        elif self.gladness <= 0:
            print("В чому сенс життя?..")
            self.alive = False
        elif self.progress >= 4:
            print("Автомат")
            self.alive = False
        elif self.money <= -50:
            print("По вас прийшли колектори!..")
            self.alive = False

    def status(self):
        if self.progress <= 0.01:
            self.to_study()
        elif self.money <= 10:
            self.to_work()

    def end_of_day(self):
        print(f"Твоє задоволення {self.gladness}")
        print(f"Ну і твій прогрес {round(self.progress, 2)}")
        print(f"На банці {round(self.money)}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(day)

        live_cube = random.randint(1, 4)

        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_work()

        self.end_of_day()
        self.is_alive()
        self.status()

ostap = Student(name="Ostap")

for day in range(365):
    if ostap.alive == False:
        break
    ostap.live(day)