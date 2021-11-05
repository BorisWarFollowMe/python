with open("text_1.txt", "w", encoding="utf-8") as f:
    my_str = " "
    while my_str != "":
        my_str = input("Введите одно или несколько слов или нажмите enter для завершения: ")
        if my_str == "":
            break
        f.write(f"{my_str}\n")

with open("text_1.txt", "r", encoding="utf-8") as f:
    my_str = f.readlines()
    for i, v in enumerate(my_str, 1):
        n = len(v.split())
        print(f"В строке: {i} слов: {n}")
    print(f"Всего строк: {i}")
