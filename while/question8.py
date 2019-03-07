while True:
    a = input("your password: ")
    if len(a) <8 or a.isalpha(): 
        print("try again")
    else: 
        print("correct")
