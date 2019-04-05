# 1
laptop = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30
}

laptop['TOSHIBA'] = 10
laptop["DELL"] += 10
laptop["MACBOOK"] -= 2
laptop["FUJITSU"] = 15
laptop["ALIENWARE"] = 5

# 2
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



total_price = 0

for key, value in laptop.items():
    single_price = value * price[key]
    print("the price of ", key, " is: $", single_price)
    total_price += single_price

print("The total price of all the laptop is: $", total_price)
    
    
    

