laptop = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30
}

# print(laptop["MACBOOK"])

for key, value in laptop.items():
    print(key, value, sep = ":")

total = 0
for i in laptop.values():
    total += i

print("Total numbers of laptop are: ", total)

laptop["FUJITSU"] = 15
laptop["ALIENWARE"] = 5

total = 0
for i in laptop.values():
    total += i


print('After add, we have:')

print(total)
