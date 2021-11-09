from time import sleep


class TrafficLight:

    __color = ""

    def running(self):
        self.__color = "Red"
        print(f"{self.__color}")
        sleep(7)
        self.__color = "Yellow"
        print(f"{self.__color}")
        sleep(2)
        self.__color = "Green"
        print(f"{self.__color}")
        sleep(7)
        return "it's work"


traffic_light = TrafficLight()
print(traffic_light.running())
