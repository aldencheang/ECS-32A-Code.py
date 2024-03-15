TAX_RATE = 8.25 
price = input("Enter price:")
price = float(price)
tax = price * (TAX_RATE / 100)
print("The price with tax is:", price+tax)



