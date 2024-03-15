#translate.py
word = input("Enter a word to translate:")
word_lower = word.lower()
vowels = "aeiou"
for letter in word_lower:
    if word_lower[0] not in vowels:
        print("Pig latin:", word_lower[1:] + word_lower[0] + "ay")
        break
    else:
        print("Pig latin:", word_lower + "way")
        break
