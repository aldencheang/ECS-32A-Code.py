# Tax rates and thresholds
LOWER_RATE = 0.1
HIGHER_RATE = 0.25

SINGLE_LIMIT = 32000
MARRIED_LIMIT = 64000

income = float(input("Enter income:"))
status = input("Enter s for single or m for married:")

if status == 's':
    if income < SINGLE_LIMIT:
        tax = LOWER_RATE * income
    else:
        tax = LOWER_RATE * SINGLE_LIMIT
        tax = tax + HIGHER_RATE * (income - SINGLE_LIMIT)
else:
    if income < MARRIED_LIMIT:
        tax = LOWER_RATE * income
    else:
        tax = LOWER_RATE * MARRIED_LIMIT
        tax = tax + HIGHER_RATE * (income - MARRIED_LIMIT)

print("The tax is", tax)
