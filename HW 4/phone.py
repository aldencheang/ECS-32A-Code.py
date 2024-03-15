#phone.py
pnum = input("Enter number as  ###-###-####:")
valid = len(pnum)
pos = 0
while valid and pos <12:
    if pos == 3:
        valid = pnum[pos] == "-"
    elif pos == 7:
        valid = pnum[pos] == "-"
    else:
        valid = pnum[pos].isdigit()
    pos = pos + 1
if valid:
    print("Valid")
else:
    print("Invalid")
