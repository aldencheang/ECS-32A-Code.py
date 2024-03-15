#parrot.py
while True:
    parrot = input(">")
    if parrot.lower() == "hush":
        break
    else:
        print(parrot.upper())
        continue
