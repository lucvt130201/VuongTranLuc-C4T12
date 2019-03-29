person = {
"name" : "Tung",
"age" : 21

}

ask = input("which one do you want to check?: ")
if ask in person:
    print("Key ", ask, " exist in my dictionary", sep = "'")
else:
    print("key ", ask, " does not exist in my dictionary", sep = "'" )
    

