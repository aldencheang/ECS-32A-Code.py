#extract.py
entry = input("Enter phone number: ")
phoneNum = ""
missing ="-() " #These letters go bye bye
for c in entry:
    if c in missing:
        c = ""
    phoneNum = phoneNum + c
print("Numbers:", phoneNum)
