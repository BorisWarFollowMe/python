n = int(input("Введите значение выручки: "))
m = int(input("Введите значение издержек: "))
v = n - m
if v > 0:
    print(f"Прибыль составила: {v}")
    print(f"Рентабельность выручки - {int((v / n) * 100)}%")
    s = int(input("Введите количество сотрудников: "))
    print(f"Прибыль фирмы в расчете на одного сотрудника: {round(v / s, 2)}")
else:
    print(f"Вы должны мафии: {-v}. Сотрудники остались голодными(((")
