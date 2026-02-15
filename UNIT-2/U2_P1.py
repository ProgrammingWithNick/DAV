'''Unit 2
Program.1:Write a program to create a list of names; then define a function to 
display all the elements in the received list. 
Call the function to execute its statements
and display all names in the list.
'''

# number of elements as input
n = int(input("Enter number of names : "))#5

#creating an empty list
names = []

# iterating till the range
for i in range(n):
	student = input("enter name:")

	names.append(student) # adding the element



#define function to print

def printl(names):
    print(names)
    return

#calling function
printl(names)



