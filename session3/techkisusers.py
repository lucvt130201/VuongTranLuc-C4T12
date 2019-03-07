name = input("username: ")
password = input("password:")

if name != "techkids":
    print("you are not supperuser")
elif name == "techkids" and password != "codethechange":
    print("Invalid password")
else:
    print("Welcom, supperuser!")
