'''P-1.6"Write a program to prompt users to enter a value;then check whether
the entered value is positive or negative value and display a proper message.'''


num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")
