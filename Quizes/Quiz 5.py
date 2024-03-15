infile = open("test.csv")
for line in infile:
    line = line.strip()
    student, grade = line.split(",")[0], line.split(",")[1]
