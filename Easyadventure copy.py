yes_no = ""
path = [0, 0]
move = ["north", "south", "east", "west"]
inventory = {
    "pocket": {
        "key": False
    }

}

while path != [0, 1]:

    
    
    if path == [0, 0]:
        print(path)
        print("You enter a large room. The two doors in the room go north and south")
        move = input("Choose north or south: ")
        print("")
        if move == "north":
            path[1] +=1
        elif path == "east":
            path[0] += 1
        elif move == "south":
         path[1] -= 1
        elif path == "west":
            path[0] -= 1
    else:
        print("Didn't get that")
    if path == [0, -1]:
        print(path)
        if inventory["pocket"]["key"] != True:
            print("You find a key on the floor. Do you want to pick it up?")
            yes_no = input("Choose yes or no: ")
            print("")

            if yes_no == "yes":
                print(path)
                inventory["pocket"]["key"] = True
                print("You picked up the key and returned to the main room.")
                print("")
                path = [0, 0]
            elif yes_no == "no":
                print(path)
                print("You return to the main room.")
                path = [0, 0]
            else:
                print(path)
                print("Invalid Response")
                print("")
                path = [0, 0]


        else:
            print(path)
            yes_no = input("There is nothing new in this room. Return to the main room? ")
            print("")
            if yes_no == "yes":
                path = [0, 0]
            else:
                path = [0, -1]


        if path == [0, 1]:
            if inventory["pocket"]["key"] == True:
                print("You escape!")
                print("")
                path = [0, 1]
                break
            else:
                print("The door is locked.")
                print("You are sill")
                print("")
                path = [0, 0]
    elif path == [0, 1]:
        if inventory["pocket"]["key"] == True:
            print("You escape!")
            print("")
            path = [0, 1]
            # break
        else:
            print("The door is locked.")
            print("")
            path = [0, 0]
    else:
        print("Invalid Response")
        print("")
        path = [0, 0]
