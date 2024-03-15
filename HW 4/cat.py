while True:
    filename = input("Enter a file name to open:")
    try:
        infile = open(filename, "r")
    except:
        print("Could not open", filename)
        continue
    break
for line in infile:
    line = line.strip()
    print(line)
