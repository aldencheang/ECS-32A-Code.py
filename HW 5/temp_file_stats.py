max_temp = 0
min_temp = 0
filename = input("Temperature anomaly filename:")
infile = open(filename, "r")
infile.readline()
for line in infile:
    lines = line.strip()
    lines = line.split(',')
    year = int(lines[0])
    temp = float(lines[1])
    if min_temp > temp:
        min_temp = temp
        min_year = year
    if max_temp < temp:
        max_temp = temp
        max_year = year
print("Min temp:", min_temp, "in", min_year)
print("Max temp:", max_temp, "in", max_year)
    
