while True:
    a = input("Your first name: ")
    b = input("Your middle name")
    c = input("Your last name")
    if a.isalpha() == True and b.isalpha() == True and c.isalpha() == True:
        print("Your full name is: ", a," ", b, " ", c)
        break
    
