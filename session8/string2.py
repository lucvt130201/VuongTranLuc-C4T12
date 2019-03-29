import random

word = input("what is your word: ").upper()
characters = list(word)
print(characters)
while True:
    if len(characters) == 0:
        break
    else:
        letter = random.choice(characters)
        print(letter)
        characters.remove(letter)
    
