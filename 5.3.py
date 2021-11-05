with open("text_3.txt", "r", encoding="utf-8") as f:
    my_dict = {s.split()[0]: float(s.split()[1]) for s in f}
    print(f"Средняя зарплата: {round(sum(my_dict.values()) / len(my_dict), 2)}")
    print("Зарплата меньше 20000 у следующих сотрудников:")
    for i in my_dict.items():
        if i[1] < 20000:
            print(f"{i[0]}")
