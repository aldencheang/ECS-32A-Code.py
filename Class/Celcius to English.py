# Celsius to English

cel = input("Enter degrees Celsius:")
cel = int(cel)

#Assign an interpration of the temperature

#Freezing cold: cel is - degrees or below
if cel <= 0:
    print("Freezing cold")
# Cold: below 10 degrees
elif cel < 10:
    print("Cold")
# Cool: below 15 degrees
elif cel <15:
    print("Cool")
# Nice: between 15 and 25 inclusive
elif cel<= 25:
    print("Nice")
# Super hot
elif cel > 40:
    print("Super hot")
# Hot: above 30 degrees
elif cel > 30:
    print("Hot")
# Warm: above 25 degrees
else: cel > 25:
    print("Warm")

