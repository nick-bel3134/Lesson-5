import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Тре зубрити")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("Хочу дрихнути")
        self.gladness += 3

    def to_chill(self):
        print("Пішов прокрастинувати")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Press F...")
            self.alive = False
        elif self.gladness <= 0:
            print("В чому сенс життя?..")
            self.alive = False
        elif self.progress >= 4:
            print("Автомат в руки...")
            self.alive = False

    def end_of_day(self):
        print(f"Твоє задоволення {self.gladness}")
        print(f"Ну і твій прогрес {round(self.progress, 2)}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(day)

        live_cube = random.randint(1, 3)

        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()

        self.end_of_day()
        self.is_alive()

ostap = Student(name="Ostap")

for day in range(365):
    if ostap.alive == False:
        break
    ostap.live(day)