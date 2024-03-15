while True:
    filename = input("Enter filename:")
    try:
        infile = open(filename)
    except:
        continue
    break
    
infile.close()
