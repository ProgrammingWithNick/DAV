# P1.6 - Check if number is Positive or Negative

number = float(input("Enter a number: "))

if number > 0:
    print(f"{number} is Positive\n")
elif number < 0:
    print(f"{number} is Negative\n")
else:
    print("The number is Zero\n")