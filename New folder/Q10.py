inword = input("Enter word:")
pirate = " Argh!"    # what the pirate will say
for c in inword:
    pirate = c.upper() + pirate
print(pirate)
