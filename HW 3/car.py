print("Guess the price and win the prize!")
count = 0
#guess
while count <= 5:
    guess = int(input("Enter your guess:"))
    if count == 5:
        print("Too many guesses!")
        break
    elif guess == 42500:
        print("You won the car!")
        break
    elif guess < 42500:
        print("Too low!")
    elif guess > 42500:
        print("Too high!")
    count = count + 1
