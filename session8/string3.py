import random

words_list = ["cho", "meo", "techkids","incubatorofchange"]
while True:
    word = random.choice(words_list).upper()
    characters = list(word)
    # print(characters)
    while True:
        if len(characters) == 0:
            break
        else:
            letter = random.choice(characters)
            print(letter, end =",")
            characters.remove(letter)

    ans =input("what is the words?: ").upper()
    if ans == word:
        print("correct")
    else:
        break

    
    
