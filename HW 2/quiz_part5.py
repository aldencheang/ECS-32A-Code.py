score = 0
#q1
print('ART AND LITERATURE: Who painted "The Birth of Venus"?\na. Botticelli\nb. Michelangelo\nc. Leonardo da Vinci')
ans1 = input("Enter your choice:")
if ans1 == "a":
    print("Correct!")
    score = score + 1
else:
    print("The correct answer was a")    
#q2
print('ENTERTAINMENT: How many oscars did Alfred Hitchcock win?\na. None\nb. One\nc. Two')
ans2 = input("Enter your choice:")
if ans2 == "a":
    print("Correct!")
    score = score + 1

else:
    print("The correct answer was a")
#q3
print('GEOGRAPHY: Which is the largest ocean?\na. Pacific\nb. Atlantic\nc. Indian')
ans3 = input("Enter your choice:")
if ans3 == "a":
    print("Correct!")
    score = score + 1
else:
    print("The correct answer was a")
#q4
print('HISTORY: Who was the first U.S. president to appear on a coin?\na. Washington\nb. Lincoln\nc. Jefferson')
ans4 = input("Enter your choice:")
if ans4 == "b":
    print("Correct!")
    score = score + 1
else:
    print("The correct answer was b")
#q5
print('SCIENCE AND NATURE: Can pigs swim?\na. Yes\nb. No\nc. Only in salt water')
ans5 = input("Enter your choice:")
if ans5 == "a":
    print("Correct!")
    score = score + 1
else:
    print("The correct answer was a")

#q6
print('SPORT AND LEISURE: What color is the middle Olympic ring?\na. Red\nb. Blue\nc. Black')
ans6 = input("Enter your choice:")
if ans6 == "c":
      print("Correct!")
      score = score + 1
else:
    print("The correct answer was c")

#q7
print("GENIUS: In ancient Rome, what is XL divided by X?")
ans7 = input("Enter your answer:")
if ans7 == ("4" or "IV"):
    print("Correct!")
    score = score + 1
else:
    print("Correct answers were 4 or IV")

#final score
print("Your final score is", score)

#score meaning
if score == 7:
    print("Genuis!")
elif score >= 5 and score <=6:
    print("You are a trivia star!")
elif score >= 3 and score <=4:
    print("You did better than chance!")
elif score >= 0 and score <=2:
    print("You were unlucky!")
