my_list = []
n = int(input("Enter the number of list items from 2 to 10: "))
if n < 2 or n > 10:
    while n < 2 or n > 10:
        n = int(input("Number of list items out of range, try again: "))
    while n != 0:
        my_list.append(input("Enter the list item: "))
        n -= 1
else:
    while n != 0:
        my_list.append(input("Enter the list item: "))
        n -= 1
print(f"The list is: {my_list}")
for i in range(0, len(my_list) - 1, 2):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(my_list)
