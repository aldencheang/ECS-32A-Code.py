outfile = open("testing.tsv", "w")
year = 2022
temp = 0.1234567
outfile.write("{}\t{:.4f}\n".format(year,temp))
outfile.close()
