class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.spd = speed
        self.clr = color
        self.nm = name
        self.isplc = is_police

    def go(self):
        if self.isplc:
            print(f"Police {self.clr} {self.nm} - go")
        else:
            print(f"{self.clr} {self.nm} - go")

    def stop(self):
        if self.isplc:
            print(f"Police {self.clr} {self.nm} - stop")
        else:
            print(f"{self.clr} {self.nm} - stop")

    def turn(self, dir):
        if self.isplc:
            print(f"Police {self.clr} {self.nm} - turn {dir}")
        else:
            print(f"{self.clr} {self.nm} - turn {dir}")

    def show_speed(self):
        if self.isplc:
            print(f"Police {self.clr} {self.nm} speed is {self.spd}")
        else:
            print(f"{self.clr} {self.nm} speed is {self.spd}")


class TownCar(Car):

    def show_speed(self):
        if self.isplc:
            print(f"Police {self.clr} {self.nm} speed is {self.spd}")
        else:
            print(f"{self.clr} {self.nm} speed is {self.spd}")
        if self.spd > 60:
            print(f"out of speed limit 60")


class WorkCar(Car):

    def show_speed(self):
        if self.isplc:
            print(f"Police {self.clr} {self.nm} speed is {self.spd}")
        else:
            print(f"{self.clr} {self.nm} speed is {self.spd}")
        if self.spd > 40:
            print(f"out of speed limit 40")


class SportCar(Car):
    pass


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(self, speed, color, name, is_police=True)


car_1 = TownCar(65, "Blue", "Lada", False)
car_2 = WorkCar(40, "Red", "Audi", False)
car_3 = SportCar(300, "Green", "Uaz", True)
car_4 = PoliceCar(560, "White", "Camry", False)
car_list = [car_1, car_2, car_3, car_4]

for i in car_list:
    print(f"{i.clr} {i.nm} {i.spd} {i.isplc}")
    i.go()
    i.stop()
    i.turn("Right")
    i.turn("Left")
    i.show_speed()
