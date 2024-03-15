filename = input("Temperature anomaly filename:")
temperature = []
infile = open(filename, "r")
infile.readline()
for line in infile:
    lines = line.strip()
    lines = line.split(',')
    year = int(lines[0])
    temp = float(lines[1])
    temperature.append(temp)
###print(temperature)

k = int(input("Enter window size:"))
for index in range(k, len(temperature) - k):
    year = 1880 + index
    ave = sum(temperature[index-k:index+k+1]) / (2*k+1)        
    print("{},".format(year)+ "{:.4f}".format(ave))
#export to csv
    outfile = open("MovingAve.csv", "w")
    outfile.write("Year,Value\n")
    year = str(year)
    outfile.write(year)
    outfile.close()
