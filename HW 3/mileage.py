print("Your Personal Fuel Economy")
mileage = 0
count = 0
nom_avg = 0
nog_avg = 0
#loop
while True:
#number of miles
    nom = input("Number of miles traveled (or enter to exit):")
    count = count + 1
    if nom == "":
        break
    nom = float(nom)
#number of gallons
    nog = float(input("Number of gallons needed:"))
    mileage = nom/nog
    print("Mileage this tank:", "{:.1f}".format(mileage))
    mileage = "{:.1f}".format(mileage)
    mileage = float(mileage)
    nom_avg = nom_avg + nom
    nog_avg = nog_avg + nog
#average
average_mileage = nom_avg/nog_avg
print("Average mileage:", "{:.1f}".format(average_mileage))
    
