a = int(input("Введите свой первый результат пробежки в км.: "))
b = int(input("Введите желаемый результат пробежки в км.: "))
print(f"1-й день: {a}км.")
n = 1
while True:
    if a < b:
        a += a * 0.1
        n += 1
        print(f"{n}-й день: {round(a, 2)}км.")
        continue
    else:
        print(f"Вы достигните желаемого результата через {n} дней")
        break
