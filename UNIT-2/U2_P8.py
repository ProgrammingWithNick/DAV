string=input("Enter string:") 

#count vowels...
vowels=0

for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1


print("Number of vowels are:",vowels)

#count length

print(len(string))
#count length without len

count = 0

for i in string:
 
    count=count + 1
print("length is",count)

#reverse string

revstr=string[::-1]
print(revstr)

#palindrome

if(string==revstr):
    print("string is palindrome")
else:
    print("not palindrome")


# find & replace
print(string)

old=input("enter old word for replace ")
new=input("enter new word ")

print(string.replace(old,new))  #  2 means num of time replace allowed



