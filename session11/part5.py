warehouse = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30

}

print(warehouse)

warehouse["TOSHIBA"] = 10
warehouse["DELL"] += 10
warehouse["MACBOOK"] -= 2
warehouse["FUJITSU"] = 15
warehouse["ALIENWARE"] = 5

print(warehouse)

ask = input("which one was be sold and how many(separated by ':')")
sold = ask.split(":")

if sold[0].upper() in warehouse:
    warehouse[sold[0].upper()] -= int(sold[1])
    print("After sold: ")
    print(warehouse)
else:
    print("This kind of laptop is not in the warehouse.")




# if sold in warehouse:
#     warehouse[sold] -= number
#     print("after sold:")
#     print(warehouse)
# else:
#     print("this laptop is not in the warehouse.")

