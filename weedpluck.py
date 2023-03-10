from random import randint
print("You enter the garden.")
board = []
weed1 = False
weed2 = False
gameover = False
for x in range(5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

# print_board(board)
def random_x(board):
  return randint(0, len(board) - 1)

def random_y(board):
  return randint(0, len(board[0]) - 1)

def random_a(board):
  return randint(0, len(board) - 1)

def random_b(board):
  return randint(0, len(board[0]) - 1)
weed_x = random_x(board)
weed_y = random_y(board)
weed_a = random_a(board)
weed_b = random_b(board)
board[weed_x][weed_y] = "|"
board[weed_a][weed_b] = "|"
yes_no = input("A guard walks up to you in the garden and asks you to pluck weeds. Will you accept? ")
if yes_no == "yes":
    gameover = False
    if gameover == False:
      print_board(board)
      for turn in range(4):
        print("Turn", turn + 1, "out of 4")
        guess_y = int(input("Guess Row: ")) - 1
        guess_x = int(input("Guess Col: ")) - 1

        if gameover == True:
          print("You won")
          
        elif guess_x == weed_x and guess_y == weed_y:
          board[weed_x][weed_y] = "X"
          print_board(board)
          print("You got the first weed!")
          weed1 = True
          if weed1 and weed2 == True:
            print("You got all the weeds!")
            print("Game Over")
            gameover = True
      
        elif guess_x == weed_a and guess_y == weed_b:
          board[weed_a][weed_b] = "X"
          print_board(board)
          weed2 = True
          print("You the second weed!")
          if weed1 and weed2 == True:
            print("You got all the weeds!")
            gameover = True

        else:
          if (guess_x < 0 or guess_x > 4) or (guess_y < 0 or guess_y > 4):
            print("Oops, that's not even in the garden.")
            turn -=1
          elif(board[guess_x][guess_y] == "X"):
            print("You guessed that one already.")
            turn -=1
          else:
            print("You missed the weed!")
            board[guess_x][guess_y] = "X"

            if turn == 3:
              print("Game Over")
              gameover = True
          print_board(board)
    else:
      print("You gained 100 Gold")
else:
  print("You decline. Where will you go next?")
  move = input("Will you go north or south? ")