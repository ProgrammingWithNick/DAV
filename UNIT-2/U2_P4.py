'''p 2.4:  Write a program to create a series to maintain
three students’ names and SPI values.'''

import pandas as pd

dict = {}

n= int(input(" Number of student: "))


for i in range(n):
    name = input("Enter student's name: ")
    mark = input("Enter mark: ")

    dict[name] = mark


# create series from dictionary
s = pd.Series(dict)
print(" series of data is")
print(s)

