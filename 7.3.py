class Cell:

    def __init__(self, cell_num):
        self.cn = cell_num

    def __add__(self, other):
        return Cell(self.cn + other.cn)

    def __sub__(self, other):
        return Cell(self.cn - other.cn if self.cn - other.cn > 0 else print("there are no cells left"))

    def __mul__(self, other):
        return Cell(self.cn * other.cn if self.cn * other.cn != 0 else print("there are no cells left"))

    def __truediv__(self, other):
        try:
            return Cell(int(round(self.cn / other.cn, 0)))
        except ZeroDivisionError:
            print("not enough cells")

    def __str__(self):
        return f"Cells - {self.cn}"

    def make_order(self, n):
        row = self.cn // n
        left = self.cn % n
        return '\n'.join('*' * n for _ in range(row)) + f"\n{'*' * left}"


cells_1 = Cell(10)
cells_2 = Cell(3)
cells_3 = cells_2 - cells_1
print(cells_3)
cells_3 = cells_1 * cells_2
print(cells_3)
print(cells_3.make_order(7))
cells_3 = cells_1 / cells_2
print(cells_3)
print(cells_3.make_order(7))
