'''P-1.1:Write a Python script to prompt users to enter two values;
then perform the basic arithmetical operations of addition,
subtraction, multiplication and division on the values'''


num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

result1 = num1 + num2
result2 = num1 - num2
result3 = num1 * num2
result4 = num1 / num2

print("add :",result1)
print("sub :",result2)
print("multiply :",result3)
print("divide :",result4)

'''
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Enter which operation would you like to perform?")
ch = input("Enter any of these char for specific operation +,-,*,/: ")

result = 0
if ch == '+':
    result = num1 + num2
elif ch == '-':
    result = num1 - num2
elif ch == '*':
    result = num1 * num2
elif ch == '/':
    result = num1 / num2
else:
    print("Input character is not recognized!")

print(num1, ch , num2, ":", result)
'''

