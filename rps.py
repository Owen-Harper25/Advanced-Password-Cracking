import random
from random import randint
i = 3
"scissors" < "rock"
"rock" < "paper"
"paper" < "scissors"

print("Welcome to the ultimate game of Rock Paper Scissors")
# while i > 0:
#     i -= 1
choice = input("Choose rock paper or scissors: ")
bot = randint (1,3)
if bot == 3:
    bchoice = "rock"
elif bot == 2:
    bchoice = "paper"
else:
    bchoice = "scissors"
print(bchoice)
print(bchoice == choice)

 
import sys # to access the system
import cv2
img = cv2.imread("sheep.png", cv2.IMREAD_ANYCOLOR)
 
while True:
    cv2.imshow("Sheep", img)
    cv2.waitKey(0)
    sys.exit() # to exit from all the processes
 
cv2.destroyAllWindows() # destroy all windows