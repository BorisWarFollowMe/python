my_list = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето",
           "Осень", "Осень", "Осень", "Зима"]
my_dict = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето",
           9: "Осень", 10: "Осень", 11: "Осень", 12: "Зима"}
n = int(input("Enter the number of month from 1 to 12: "))
if n < 1 or n > 12:
    while n < 1 or n > 12:
        n = int(input("Number of month is wrong, try again: "))
n -= 1
print(my_list.pop(n))
n += 1
print(my_dict.pop(n))
