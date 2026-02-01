# w a p find square of give range

start = int(input("Enter starting value: "))
end = int(input("Enter ending value: "))

for i in range(start, end + 1):
    print("Square of", i, "is", i * i)