def odd_sum(n):
    oddOnly = 0
    for number in range(1,n+1):
        if number % 2 != 0: 
            oddOnly = oddOnly + number
    return oddOnly

result = odd_sum(99)
print(result)
