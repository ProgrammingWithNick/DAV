'''P1.5:Write a program to prompt users to enter their working hours and rate
per hour to calculate gross pay.
The program should give the employee 1.5 times the hours worked above 30 hours.
If Enter Hours is 50 and Enter Rate is 10,
then the calculated payment is Pay: 550.0.'''


hrs = float(input("Enter Hours:"))
rate =float(input("Enter the Rate:"))
if hrs <= 30:
 	print( hrs  * rate)
elif hrs > 30:
	print(30* rate + (hrs-30)*1.5*rate)
