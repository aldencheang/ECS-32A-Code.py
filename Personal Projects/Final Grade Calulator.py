#Final Grade Calculator
#
#
grade = float(int(input("What is your current grade in %: ")))
weight = float(int(input("What is your final worth in %: ")))
want = float(int(input("What grade do you want in %?: ")))

formula = str((((want - (1 - (weight / 100)) * grade)/ weight) * 100))

print("You need to get", formula + "% on the exam to get a", str(want) + "% in the class")
