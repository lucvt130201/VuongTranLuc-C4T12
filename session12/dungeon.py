player = {
    'x': 1,
    'y': 2
}

key = {
    'x': 3,
    'y': 2
}

Door = {
    'x': 2,
    'y': 1
}

size_map = {
    'size_x': 4,
    'size_y': 4
}

check = False
while True:
    for y in range(size_map['size_y']):
        for x in range(size_map['size_x']):
            if y == player['y'] and x == player['x']:
                print("P", end = " ")
            elif y == Door['y'] and x == Door['x']:
                print("E", end = " ")
            elif y == key['y'] and x == key['x']:
                print("K", end = " ")
            else:
                print("-", end = " ")
        print()

    move = input("Your move: ").upper()

    dx = 0
    dy = 0

    if move == "D":
        dx = 1
    elif move == "A":
        dx = -1
    elif move == "W":
        dy = -1
    elif move == "S":
        dy = 1


    # Limit Map:
    if 0 <= player['x'] + dx < size_map['size_x']:
        player['x'] += dx
    else: 
        print("cannot move out the map")

    if 0 <= player['y'] + dy < size_map['size_y']:
        player['y'] += dy
    else: 
        print("cannot move out the map.")

    #  Find E:
    if player['x'] == Door['x'] and player['y'] == Door['y']:
        if check == True:
            print("Congrats!!!")
            break
        else:
            print("Find the key first")

    # Find K:
    if player["x"] == key["x"] and player['y'] == key['y']:
        print("Now you have the key, find the door")
        key['x'] = 5
        key['y'] = 5
        check = True
    else:
        if check == False:
            print("You can't exit, please aquire the key first.")


