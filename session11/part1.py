laptop = {
    "HP" : 20,
    "Dell" : 50,
    "Macbook" : 12,
    "Asus" : 30

}

# PART I
ask = input("which laptop do you want to know?: ")
print("we have: ", laptop[ask])

# PART II
ask2 = input("which laptop do you want to add?: ")
number = int(input("How many do you want to add?: "))

laptop[ask2] = number

print(laptop)

laptop["Dell"] += 10
laptop["Macbook"] += 2

print(laptop)

