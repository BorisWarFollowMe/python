my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("new_text_4.txt", "w", encoding="utf-8") as nf:
    with open("text_4.txt", "r", encoding="utf-8") as f:
        nf.writelines([line.replace(line.split()[0], my_dict.get(line.split()[0])) for line in f])
