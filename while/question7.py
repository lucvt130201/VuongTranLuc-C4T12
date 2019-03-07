while True:
    p = input('Your password: ')
    if p.isalpha() == True:
        print("Wrong password. Enter again.")
    if p.isalpha() == False:
        print("continue")
        break
