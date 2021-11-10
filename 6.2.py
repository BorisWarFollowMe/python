

class Road:

    def __init__(self, lengh, width):
        self._len = lengh
        self._wid = width

    def what_mass(self):
        return self._wid * self._len * 25 * 5 / 1000


road_1 = Road(5000, 20)
print(f"{int(road_1.what_mass())}т.")
