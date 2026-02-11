'''P-1.8:Write a program to prompt users to enter an age; then check whether
each person is a child, a teenager, an adult, or a senior.
Display a proper message.'''

age = int(input("Please enter your age:"))
if age <= 0:
	print('Invalid input')
elif age >= 1 and age <= 5:
	print('Infant')
elif age >= 6 and age <= 10:
	print('Child')
else:
	print('Adult')
