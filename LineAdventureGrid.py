#Imports
import random
from random import randint
move = ["north", "south", "east", "west"]
yes_no = ["yes", "no"]
attack = ["slash", "stab", "run"]
path = [0, 0]
pdrink = False

#Inventory
inventory = {
    "backpack" : {
        "poison_powder" : 1,
        "sword" : False
    },
    "gold" : 100
}

#Story
print("Welcome to your adventure! Enter your name to start.")
name = input("Insert Name: ")

while path != [0 ,2]:
    
    print("You enter the castle's long hallway. To the East is the king's throne room and to your West is the royal kitchen. The guard's barracks is to the north. Choose your path", name, "the adventurer.")
    move = input("Enter north, east, south, or west: ")
    if move == "north":
        path[1] +=1
    elif move == "east":
        path[0] += 1
    elif move == "south":
        path[1] -= 1
    elif move == "west":
        path[0] -= 1

    if path == [-1, 0]:
        print("You choose to enter the castle's kitchen. Inside the warm and cluttered room, there are multiple chefs preparing the royal familie's dinner." \
        " They are focused on cooking and don't seem to notice you. If you want, you are able to put a vile of poison powder in the wine barell that will "\
        "be fed to the king but risk getting caught. Will you poison the king's wine?")
        yes_no = input("Choose yes or no: ")

        if yes_no == "yes" and inventory["backpack"]["poison_powder"] > 0:
            roll = (random.randrange(1, 10))
            if roll == 1:
                print("The chefs notice you and call the guards. You are hastily throne in the dungeon for your attemted treason.")
                print("Game Over")
                break
            else:
                inventory["backpack"]["poison_powder"] -= 1
                print("You poison the king's drink and haistly leave the kitchen.")
                pdrink = True
                path = [0, 0]
        elif yes_no == "yes":
            print("You don't have any poison left. You leave the kitchen.")
            path = [0, 0]
        elif yes_no == "no":
            print("You decide against posining the wine and leave the kitchen. You are now in the main hall again.")
            # print(inventory["backpack"]["poison_powder"])
            path = [0, 0]
        else:
            print("Invalid response")
            # print(inventory["backpack"]["poison_powder"])
            path = [0, 0]
    elif path == [0, 1]:
        print("You enter the barracks.")
        if inventory["backpack"]["sword"] == False:
            print("You There is a sword laying against the wall, do you want to pick it up?")
            yes_no = input("Choose yes or no: ")
            if yes_no == "yes":
                print("You pick up the sword and mount it on your back.")
                inventory["backpack"]["sword"] = True
                print("Nothing else catches your eye so you leave the room.")
                path = [0, 0]
            elif yes_no == "yes" and inventory["backpack"]["sword"] == True:
                print("There is nothing else useful in this room.")
                path = [0, 0]
            else:
                print("You descide to leave the sword alone. Nothing else catches your eye so you leave the room.")
                path = [0, 0]
        else:
            print("There is nothing else useful in this room.")
            path = [0, 0]
    elif path == [1, 0] and pdrink == True:
        print("The king is laying on the floor with guards running franticly shouting that the king has died. You look at the kings hand to see a broken wine glass.")
        print("You win!")
        break
    elif path == [1, 0] and inventory["backpack"]["sword"] == True:
        print("As you are entering the throne room you pull out the sword you found and the guards rush at you. There are two guards near the king, how do you respond?")
        attack = input("Do you slash, stab, or run? ")
        if attack == "run":
            print("You instantly regret pulling out the sword and are intimidated by the strong looking guards. You immidiatly turn around and sprint \
            out of the castle to live another day.")
            break
        elif attack == "slash":
            print("You swing your sword sideways and it gets deflected by the guard's metal armour. The two guards stab you and you die.")
            print("Game Over")
            break
        elif attack == "stab":
            print("You thrust your sword deep into on guard's chest and then pull it out whilst doing a round house kick that lands on the second \
            guard's head. He falls to the ground and you finish him off. The king pleads to you to spare him, but you don't.")
            print("You gain 5000 gold for slaying the enemy king.")
            inventory["gold"] + 5000
            print("You win!")
            break
    elif path == [0, -1]:
        print("You enter the garden.")
        yes_no = input("Talk to the guard standing in the corner? ")
        if yes_no == "yes":
            print("You walk up to the guard. He asks you to pluck weeds in the garden.")
            yes_no = input("Will you accept? ")
        else:
            print("You decline. Where will you go next?")
            move = input("Will you go north or south? ")


    elif path == [1, 0]:
        print("You enter the throne room and you are in the presence of the king. You bow to the king, and he tells you to scram since you are wasting his time.\
            the king's guards throw you back into the main hallway.")
        path = [0, 0]
    else:
        print("Invalid Response")
        path = [0, 0]