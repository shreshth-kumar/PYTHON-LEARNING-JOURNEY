#WAP to find the greatest of 3 numbers entered by the user.

a = int(input("enter your first number: "))
b = int(input("enter your second number: "))
c = int(input("enter your third number: "))

if(a >= b and a >= c):
    print("first number is largest", a)
elif(b >= c):
    print("second number is largest", b)
else:
    print("third number is largest", c)