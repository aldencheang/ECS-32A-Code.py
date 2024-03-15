s = input("Enter a proper noun:")
proper_case = s[0].isupper() and s[1:].islower()
if not proper_case:
   print("Incorrect case for a proper noun!") 
