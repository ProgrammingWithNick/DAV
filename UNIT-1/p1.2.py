'''P-1.2:Write a Python script to prompt users to enter the
first and last values and generate some random values
between the two entered values'''



import random
n=int(input("how many random values you want"))
l=int(input("lower range"))
u=int(input("upper range"))      
for i in range(n):
    x = random.randint(l,u)
    print(x)



'''import random
n=int(input("how many random values you want"))
l=int(input("lower range"))
u=int(input("upper range")) 

x = random.sample(range(l,u),n)

print(x)


'''




"""
import random

mylist = []

for i in range(0,100):
    x = random.randint(1,10)
    mylist.append(x)

print(mylist)

"""
