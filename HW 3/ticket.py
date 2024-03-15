age = int(input("Enter age:"))
if age < 3:
    print("Price: FREE")
elif age >= 3 and age <= 12:
    print("Price: $39.95")
elif age >= 13 and age <= 17:
    print("Price: $39.95")
elif age >=18 and age <=64:
    ID = input("College ID? (y/n)")
    if ID == "y":
        print("Price: $39.95")
    else:
        print("Price: $49.95")
elif age >= 65:
    print("Price: $39.95")

