numbers = [5, 1, 8, 92, -1, 30]

ask = int(input("What is your number?: "))

if ask not in numbers:
    print("Not found in our list!")
else:
    position = 0
    
    for i in numbers:
        position +=1
        if ask == i:
            print("Found, position", position)
            break
                

    
