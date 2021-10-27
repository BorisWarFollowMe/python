def my_def(a1, a2, a3):
    my_list = [a1, a2, a3]
    my_list.sort(reverse=True)
    my_sum = my_list[0] + my_list[1]
    return my_sum


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
print(my_def(a, b, c))
