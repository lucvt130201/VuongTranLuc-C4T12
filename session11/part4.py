price = {
    "HP" : 600,
    "DELL" : 650,
    "MACBOOK" : 12000,
    "ASUS" : 400,
    "ACER" : 350,
    "TOSHIBA" : 600,
    "FUJITSU" : 900,
    "ALIENWARE" : 1000
}

ask = input("Which laptop do you want to know?: ").upper()
if ask in price:
    print("the price of this laptop is: $", price[ask])
else: 
    print("We do not have this laptop in our dictionary.")
    

ask2 = input("Which laptop do you want to buy?: ").upper()
if ask2 in price:
    number = int(input("How many do you want to buy?: "))
    total = price[ask2] * number
    print("You should pay: $", total)
else:
    print("We do not have this laptop.")

