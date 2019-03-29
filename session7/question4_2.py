while True:
    email = input("your email: ")
    if "@" not in email:
        print("Your email must have @, .")
    elif "." not in email:
        print("your email must have @, .")
    else:
        print(email)
        break


print(input("user name: "))


while True:    
    password = input("password: ")
    if len(password) >= 8 and password.isdigit() == False and password.isalpha()==False:
        break


while True:
    password2 = input("Re-enter your password: ")
    if password == password2:
        print('registration success')
        print("password: ")
        for i in range(len(password)):
            print("*", end ="")
            
        break
    else:
        print("your re-enter password is wrong!")