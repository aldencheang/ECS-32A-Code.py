#converter.py
char = input("Enter a character:")
num = ord(char)
binary = bin(num)
print(char, "corresponds to the integer", num, "which is", binary, "in binary.")
