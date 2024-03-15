#hybrid.py
#Cost of Car
cost = float(input("Cost of car:"))
#Miles driven per year
miles = float(input("Miles driven per year:"))
#Cost of gas
gas_cost = float(input("Cost of gas:"))
#Fuel efficiency (mpg)
mpg = float(input("Fuel efficiency (mpg):"))
#Estimated resale value after 5 years
resale = float(input("Estimated resale value after 5 years:"))
##############Calulations################
#Cost of gas per year
GPY = miles / mpg * gas_cost
#Cost of gas for 5 years
G_Five = GPY * 5
#Cost of car after selling in 5 years
car_cost = cost - resale
###############Results###############
print("Five year gas cost:", G_Five)
print("Five year car cost:", car_cost)
print("Five year total cost:", G_Five + car_cost)
