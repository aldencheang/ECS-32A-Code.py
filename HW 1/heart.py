#heart.py

age = int(input("Enter your age:"))
bpm = 220 - age
heartrate_1 = bpm * .5
heartrate_2 = bpm * .85
print("Your maximum heart rate is", bpm, "bpm" + "\nYour target heart rate is", heartrate_1, "-", heartrate_2, "bpm")
