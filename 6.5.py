class Stationery:

    def __init__(self, title="Unknown"):
        self.ttl = title

    def draw(self):
        print(f"{self.ttl}")


class Pen(Stationery):

    def draw(self):
        print(f"Draw with {self.ttl} pen.")


class Pencil(Stationery):

    def draw(self):
        print(f"Draw with {self.ttl} pencil.")


class Handle(Stationery):

    def draw(self):
        print(f"Draw with {self.ttl} handle.")


pen = Pen("Firm-1")
pencil = Pencil("Firm-2")
handle = Handle("Firm-3")
my_list = [pen, pencil, handle]

for i in my_list:
    i.draw()
