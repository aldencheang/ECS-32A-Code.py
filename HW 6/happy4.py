# happy_stubs.py


def main():

    # Part 1
    # Build dictionary mapping countries to happiness index
    happy_dict = make_happy_dict()
    
    # Part 2
    # Print key value pairs sorted by key
    # Uncomment the function call below for part 2 only
    # print_sorted_dictionary(happy_dict)

    # Part 3
    # Uncomment the function call below for part 3 only
    # lookup happiness by country until the user enters done
    # lookup_happiness_by_country(happy_dict)

    # Parts 4-6
    # Uncomment the function call below for parts 4-6 
    # Read file containing population and GDP data and add happiness data
    read_gdp_data(happy_dict)



def make_happy_dict():
    happy_dict = {}
    infile = open("happiness.csv")
    infile = infile.readlines()[1:]
    for line in infile:
        line = line.strip()
        line = line.split(",")
        happy_dict[line[0]]=line[2]
        ##print(line[0], line[2])
    return happy_dict

def read_gdp_data(happy_dict):
    data = []
    infile = open('world_pop_gdp.tsv')
    infile = infile.readlines()[0:]
    for line in infile:
        line = line.strip()
        country,pop,gdp = line.split("\t")
        line = line.strip("\n")
        pop = pop.replace(",","")
        gdp = gdp.replace("$","")
        gdp = gdp.replace(",","")
        print(country+","+pop+","+gdp)

    
    #where x is the variable we are placing
        
    return happy_dict

def lookup_happiness_by_country(happy_dict):
    while True:
        country = input("Enter a country to lookup or 'done' to exit:")
        if country in happy_dict:
            print(happy_dict[country])
        elif country == 'done':
            break
        else:
            print(country, "not found")
            continue
    
    return

# Function prints all the values in a dictionary d sorted by key
def print_sorted_dictionary(D):
    if type(D) != type({}):
        print("Dictionary not found")
        return
    print("Contents of dictionary sorted by key.")
    print("Key","Value")
    for key in sorted(D.keys()):
        print(key, D[key])
        
main()