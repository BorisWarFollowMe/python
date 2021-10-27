def my_def(x, y):
    my_exp = 1
    while y != 0:
        my_exp *= x
        y -= 1
    return 1 / my_exp


a = float(input("Enter a real number: "))
b = abs(int(input("Enter a negative degree value: ")))
print(my_def(a, b))
