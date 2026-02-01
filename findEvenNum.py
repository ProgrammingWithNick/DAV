# w a p find even number up to enter value

n = int(input("Enter a number: "))

print("Even numbers are:")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)