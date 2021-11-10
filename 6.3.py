class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.nm = name
        self.snm = surname
        self.pos = position
        self._incm = {"Wage": wage, "Bonus": bonus}


class Position(Worker):

    def get_total_name(self):
        return f"{self.nm} {self.snm}"

    def get_total_income(self):
        return sum(self._incm.values())


pos_1 = Position("Ivan", "Ivanov", "Manager", 40000, 40000)
print(pos_1.pos)
print(pos_1.nm)
print(pos_1.snm)
print(pos_1.get_total_name())
print(f"{pos_1.get_total_income()}р.")
