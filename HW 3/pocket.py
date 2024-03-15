print("Pocket change calculator")
#quarters
q = float(input("How many quarters?"))
#dimes
d = float(input("How many dimes?"))
#nickels
n = float(input("How many nickels?"))
#pennies
p = float(input("How many pennies?"))
#total
total = q/4 + d/10 + n/20 + p/100
formatted_str = "${:.2f}".format(total)
print("You have " + formatted_str)
