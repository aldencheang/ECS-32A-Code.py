print("Cash register")
total = 0
price = 0
count = 0
#input of price of item
while True:
    price = input("Enter the price of an item:")
    count = count + 1
    if price == '':
        break
    num = float(price)
    total = total + num
print("You entered", count - 1, "items totaling", "${:.2f}".format(total))
    

