my_list = [7, 5, 3, 3, 2]
n = int(input("Enter the number: "))
p1 = n in my_list
if p1:
    i = my_list.count(n)
    v = my_list.index(n)
    my_list.insert(i + v, n)
else:
    my_list.append(n)
    my_list.sort(reverse=True)
print(my_list)
