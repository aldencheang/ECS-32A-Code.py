change = int(input("Enter change:"))
#quarters
q = change // 25
print("Quarters:", q)
q = change % 25
#dimes
d = q // 10
print("Dimes:", d)
d = q % 10
#nickels
n = d // 5
print("Nickels:", n)
n = d % 5
#pennies
p = n // 1
print("Pennies:", p)


