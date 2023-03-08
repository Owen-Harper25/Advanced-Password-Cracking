yes_no = ""
path = [0, 0]
move = ["north", "south", "east", "west"]
inventory = {
    "pocket": {
        "key": False
    }

}

while path != [0, 1]:
    path = [0, 0]
    print("You enter a large room. The two doors in the room go north and south")
    path = input("Choose north or south: ")
    print("")

    if path == "south":
        path = [0, -1]
        if inventory["pocket"]["key"] != True:
            print("You find a key on the floor. Do you want to pick it up?")
            yes_no = input("Choose yes or no: ")
            print("")

            if yes_no == "yes":
                inventory["pocket"]["key"] = True
                print("You picked up the key and returned to the main room.")
                print("")
                path = [0, 0]
            elif yes_no == "no":
                print("You return to the main room.")
                path = [0, 0]
            else:
                print("Invalid Response")
                print("")
                path = [0, 0]


        else: 
            yes_no = input("There is nothing new in this room. Return to the main room? ")
            print("")
            if yes_no == "yes":
                path = [0, 0]
            else:
                path = [0, -1]


        if path == "north":
            if inventory["pocket"]["key"]:
                print("You escape!")
                print("")
                break
            else:
                print("The door is locked.")
                print("")
                path = ""
    elif path == "north":
        if inventory["pocket"]["key"] == True:
            print("You escape!")
            print("")
            break
        else:
            print("The door is locked.")
            print("")
            path = ""
    else:
        print("Invalid Response")
        print("")
        path = ""
