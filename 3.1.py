def my_def(a1, a2):
    try:
        return a1 / a2
    except ZeroDivisionError:
        return "ZeroDivisionError"


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(my_def(a, b))
