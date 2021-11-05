with open("text_6.txt", "r", encoding="utf-8") as f:
    text = f.readlines()
    for s in text:
        text_1 = "".join(i if i in "1234567890" else " " for i in s)
        text_2 = [int(i) for i in text_1.split()]
        print(f"{s.split()[0]} {sum(text_2)}ч.")
