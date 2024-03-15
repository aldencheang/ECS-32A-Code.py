total = float(input("Enter total bill:"))
#tip percent loop
pct = 15
while pct <= 25:
    print("{:.0f}%".format(pct), "is", "${:.2f}".format(total*pct/100))
    pct = pct + 1

