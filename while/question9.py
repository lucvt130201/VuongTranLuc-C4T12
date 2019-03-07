while True: 
    p = input("Your password:")
    if len(p) <8 or p.isalpha() == True or p.isdigit() == True or p.islower() == True or p.isupper() == True:
        print("try again")
    else:
        break