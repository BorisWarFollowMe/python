my_str = input("Enter a string of several words: ")
my_list = my_str.split(" ")
n = 1
for i in my_list:
    print(f"{n} {i[0:10]}")
    n += 1
