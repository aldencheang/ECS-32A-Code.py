print("Cash register")
filename = input("Enter file of prices:")
infile = open(filename, "r")
nums = [] 
for line in infile:
    line = line.strip()
    num = float(line)
    nums.append(num)
format_this = sum(nums)
formatted = "${:.2f}".format(format_this)
print("File contained", len(nums), "items totaling", formatted)
