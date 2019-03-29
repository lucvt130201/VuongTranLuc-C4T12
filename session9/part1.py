colors = ["blue", "red", "teal", "green"]
print('our color list: ')
print(*colors, sep = ", ")

ask = input("what color(s) do you want to add?: ")
colors.append(ask)
print(*colors, sep = ", ")