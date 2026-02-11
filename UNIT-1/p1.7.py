'''P-1.7 Write a program to prompt users to enter a value; then check whether
the entered value is odd or even and display a proper message.'''

num = int(input("Enter a number: "))
mod = num % 2
if num % 2 > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")
