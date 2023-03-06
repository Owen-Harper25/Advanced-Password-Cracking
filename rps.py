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

 
