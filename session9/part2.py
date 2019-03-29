# create
colors = ["blue", "red", "teal", "green"]

ask = int(input("which position do you want to know?:"))
if ask > (len(colors)-1):
    print("there is no color in this position.")
else:
    print(colors[ask - 1])

# delete
ask_2 = input("where/what do you want to delete?")
if ask_2.isdigit() == True:
    if int(ask_2) > (len(colors)-1):
        print("no color in this position")
    else: 
        colors.pop(int(ask_2)-1)
        print(*colors, sep = ", ")
if ask_2.isalpha() == True:
    if ask_2 not in colors:
        print("This color is not in the list!")
    else:
        colors.remove(ask_2)
        print(*colors, sep = ', ')



