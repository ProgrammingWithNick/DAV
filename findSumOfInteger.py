# w a p find sum of integer range

start = int(input("Enter starting value: "))
end = int(input("Enter ending value: "))

total = 0
for i in range(start, end + 1):
    total += i

print("Sum of integers =", total)