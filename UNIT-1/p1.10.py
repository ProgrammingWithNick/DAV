'''P-1.10:Write a program to prompt users to enter a Fibonacci sequence.'''


num =int(input("enter the number of terms for series"))#5


n1, n2 = 0, 1

print("Fibonacci Series:", n1, n2,end=" ")

for i in range(2, num): #5
    n3 = n1 + n2 #0+1=1
    n1 = n2 
    n2 = n3 
    print(n3, end=" ")#1
