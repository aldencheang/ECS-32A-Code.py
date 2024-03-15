#Paint Calculator
print("Paint coverage estimator")
length = int(input("Length of room in inches:"))
width = int(input("Width of room in inches:"))
height = int(input("Average height of room in inches:"))
sq = (length + width + height) // 100
print("You'll want", (sq + 1), "cans.")
