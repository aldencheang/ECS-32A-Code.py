count = 0

#initial
initial = float(input("Enter an initial Roth IRA deposit amount:"))
ret = initial
#annual rate of return
arot = float(input("Enter an annual percent rate of return:"))
while True:
    count = count + 1
    interest = ret * (arot / 100) / 12
    ret = ret + interest
    print("Value after month", str(count) + ":", "${:.2f}".format(ret))
    if ret >= initial*2:
        break
print("It will take", count, "months to double your investment with a", "{:.0f}%".format(arot), "return.")
