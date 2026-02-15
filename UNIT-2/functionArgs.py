'''print("-------------------Defult Arguments--------------------")

def product(name,price=1000):
    print("Product name is " ,name ," price is : ",price )
product('abc')

print("-------------------Required Arguments--------------------")
def family(b,s):
    print("Brother Name is : ",b," Sister Name is : ",s ,"\n")

family("Khushi","Yuvraj")#calling a fuction

print("-------------------Keyword Arguments--------------------")
def family(b,s):
    print("Brother Name is : ",b," Sister Name is : ",s ,"\n")

family(s="Khushi",b="Yuvraj")#calling a fuction
'''
def student(name,*details):
#name,age,div,enroll,------ = variable length (unknown length)
    print('Name:  ' ,name)
    print('Details of student : ' ,details)

#call a function
student('Mahi',7,'1st','Podar Int')
student('Khushi',9,'4th','Global int','NCC')






















