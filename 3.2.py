def my_def(fn, ln, ba, cr, em, pn):
    return fn + ", " + ln + ", " + ba + ", " + cr + ", " + em + ", " + pn


a = input("Enter your first name: ")
b = input("Enter your last name: ")
c = input("Enter your birth age: ")
d = input("Enter your city of residence: ")
e = input("Enter your email: ")
f = input("Enter your phone number: ")
print(my_def(fn=a, ln=b, ba=c, cr=d, em=e, pn=f))
