

#static tuple
tup1 = (1,2,3)

tup2 = (4,5,6)

if(tup1<tup2):
    print("tup1 is less than tup2")
elif (tup1==tup2):
    print("both are same")
else:
    print("tup2 is less than tup1")















'''
import numpy as np

# initialize tuples
tup1 = (100, 400, 500)
tup2 = (1300, 1000, 1800)

# printing original tuples
print("The original tuple 1 : ",str(tup1))
print("The original tuple 2 : ",str(tup2))

# Comparing tuples
# using numpy.greater()
res = all(np.greater(tup2,tup1))

res2 =(np.greater(tup2,tup1))

# printing result
print("Are all elements in second tuple greater than first ? : ",str(res))
print("Are all elements in second tuple greater than first ? : ",str(res2))


#tuple from user input
tup1 = input('Enter the tuple : ')
tup1 = tuple(int(a) for a in tup1.split(","))
print(tup1)

tup2 = input('Enter the tuple : ')
tup2 = tuple(int(a) for a in tup2.split(","))
print(tup2)

'''
