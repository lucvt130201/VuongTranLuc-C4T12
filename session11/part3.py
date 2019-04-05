laptop = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30
}

# print(laptop["MACBOOK"])

for key, value in laptop.items():
    print(key, value, sep = ":")

while True: 

    total = 0
    for v in laptop.values():
        total += v
    
    print("total number of computer is: ", total)

    new_computer = input("Enter the label of the computer: ").upper()
    number = int(input("enter the number of computers: "))
    laptop[new_computer] = number


