# Print a new word without vowels

no_vowels = ""
user_word = input("Type in a word, please: ")
user_word = user_word.upper()  # Another method...

for letter in user_word:
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue
    no_vowels += letter

print(no_vowels)
