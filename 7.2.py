from abc import ABC, abstractmethod


class Clothes(ABC):

    summary = 0

    def __init__(self, size):
        self.s = size

    def __add__(self, other):
        Clothes.summary += self.consumption + other.consumption
        return Suit(0)

    def __str__(self):
        s = Clothes.summary
        Clothes.summary = 0
        return f"{s if s > 0 else self.consumption}"

    @property
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):

    @property
    def consumption(self):
        return round(self.s / 6.5 + 0.5, 2)


class Suit(Clothes):

    @property
    def consumption(self):
        return round(self.s * 2 + 0.3, 2)


suit_1 = Suit(1.88)
coat_1 = Coat(50)
print(suit_1)
print(coat_1 + suit_1 + suit_1 + suit_1)
