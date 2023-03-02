#Imports
from random import randint


#Inventory
inventory = {
    "gold" : 0,
    "backpack" : ["Poison Powder"]

}



#Story
print("Welcome to your adventure! Enter your name to start.")
name = input("Insert Name: ")
position = "hallway"

if position == "hallway":
    print("You find yourself in a castle hallway. To your right is the king's throne room and to your left is the royal kitchen. Choose your path", name, "the adventurer.")
    path = input("Enter kitchen or throne: ")

    if path == "kitchen":
        position = "kitchen"
        print("You choose to enter the castle's kitchen. Inside the warm and cluttered room, there are multiple chefs preparing the royal familie's dinner." \
        " They are focused on cooking and don't notice you. If you want, you are able to put a vile of poison powder in the wine barell that will be fed to the king.")
        poison = input("Enter poison or leave: ")

        if poison == "poison":
            inventory["backpack"].remove("Poison Powder")
            print("You poison the king's drink and haistly leave the kitchen.")
            position = "hallway"

        else:
            position = "hallway"
            print("You decide against posining the wine and leave the kitchen. You are now in the main hall again.")

    else:
        position = "throne"
        print("You enter the throne room and you are in the presence of the king.")

else:
    print("Not in hallway")