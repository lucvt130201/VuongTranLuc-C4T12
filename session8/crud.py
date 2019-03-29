items =["cơm", "cháo", "phở"]
print(*items, sep = ', ')
while True:
    ask = input("C,R,U,D, which one do you want?: ")

    if ask == "C":
        add = input('What do you want to add?: ')
        items.append(add)
        print(*items, sep = ", ",)

    elif ask == "R":
        if len(items) == 0:
            print("The menu is empty")
        else:
            for i, item in enumerate(items):
                print(i+1,".", item)

    elif ask == "U":
        position = int(input("which position do you want to update?: "))
        if position > (len(items) - 1):
            print("no item in this position")
        else:
            update = input("what do you want to update?")
            items[position - 1] = update
            print(*items, sep = ", ")

    elif ask == "D":
        if len(items) == 0:
            print("No element to delete")
        else:
            position  = int(input("which position do you want to delete?: "))
            if position > (len(items)-1):
                print("no item in this position.")
            else:
                items.pop(position - 1)
                print(*items, sep = ", ")










