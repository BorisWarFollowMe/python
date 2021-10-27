def my_def(my_str):
    for i in my_str:
        if 122 < ord(i) or 97 > ord(i):
            return None
    return my_str.title()


my_sent = input("Enter a several words: ").split(" ")
new_sent = ""
for n in my_sent:
    if n != "" and str(my_def(n)) != "None":
        new_sent += my_def(n) + " "
print(new_sent)
