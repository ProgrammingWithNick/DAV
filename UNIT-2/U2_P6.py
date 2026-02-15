'''p2.6:Write a program in python to swap two variables
without using temporary variable'''



a=int(input("Enter value of first variable: "))
b=int(input("Enter value of second variable: "))

a,b=b,a
print("a is:",a," b is:",b)
