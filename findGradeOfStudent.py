# write a program to print grade of student(if present graterthane 90 so A+,70to 90 so first class,60 to 69 second class, 50 to 59 3th class, less than 50 so fail).

percent = float(input("Enter percentage: "))

if percent > 90:
    print("Grade: A+")
elif percent >= 70:
    print("Grade: First Class")
elif percent >= 60:
    print("Grade: Second Class")
elif percent >= 50:
    print("Grade: Third Class")
else:
    print("Grade: Fail")
