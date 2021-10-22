my_list = [11, 1.1, "string", False, [11, 1.1]]
print(my_list)
for i in my_list:
    print(f"{my_list.index(i) + 1} элемент списка имеет тип {type(i)}")
