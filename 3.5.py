def my_def():
    global s, k, my_list
    for i in my_list:
        try:
            if i == "q":
                k = False
                return
            elif i != "":
                s += int(i)
        except ValueError:
            print("Error")


k = True
s = 0
while k:
    my_list = input("Enter some numbers with a space(example: 1 2 3 4), print 'q' for stop: ").split(" ")
    my_def()
    print(f"Total: {s}")
    my_list.clear()
