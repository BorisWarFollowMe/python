import json

with open("text_7.txt", "r", encoding="utf-8") as f:
    with open("json_text_7.json", "w", encoding="utf-8") as nf:
        my_dict = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f}
        json.dump([my_dict, {"Average_profit": sum([int(i) for i in my_dict.values() if int(i) > 0]) /
                                               len([int(i) for i in my_dict.values() if int(i) > 0])}],
                  nf, ensure_ascii=False, indent=4)
