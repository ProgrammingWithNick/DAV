# P1.5 - Calculate Gross Pay

hours = float(input("Enter working hours: "))
rate = float(input("Enter rate per hour: "))

if hours > 30:
    # Regular pay for first 30 hours + overtime (1.5x) for remaining hours
    gross_pay = (30 * rate) + ((hours - 30) * rate * 1.5)
else:
    gross_pay = hours * rate

print(f"Gross Pay: ${gross_pay:.2f}")