

n=int(input("Enter the number of elements to be in the list:"))


data=[]

for i in range(0,n):
    element=int(input("ENTER Element: "))
    data.append(element)


even=[]
odd=[]

for i in data:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)

even.sort()
odd.sort()
print(even)
print(odd)
print(max(odd))
