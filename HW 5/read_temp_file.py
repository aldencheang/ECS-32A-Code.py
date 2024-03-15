filename = input("Temperature anomaly filename:")
infile = open(filename, "r")
infile.readline()
for line in infile:
    lines = line.strip()
    lines = line.split(',')
    year = int(lines[0])
    temp = float(lines[1])
    print(year, temp)
