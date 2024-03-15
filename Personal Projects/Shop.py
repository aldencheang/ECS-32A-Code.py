import random
counter = 6
lst = [1, 2, 3, 4, 5, 6]
while counter <= 6:
    counter = counter - 1
    lst.pop(random.randrange(len(lst)))
    print(lst)
    
