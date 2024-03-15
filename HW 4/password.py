#password.py
password = input("Enter password:")
#length
length = len(password)
print("Length:", length)
for letter in password:
    #lower
    if letter.islower():
        print("Has lower case")
        break
for letter in password:
    #upper
    if letter.isupper():
        print("Has upper case")
        break
for letter in password:
    #digit
    if letter.isdigit():
        print("Has digit")
        break
for letter in password:
    #special
    if letter in "@#$*!":
        print("Has special")
        break

