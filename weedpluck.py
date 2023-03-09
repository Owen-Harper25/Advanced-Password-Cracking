from random import randint

board = []

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
# weed_location = "Weed Located at {}, {}".format(weed_x + 1, weed_y + 1)
board[weed_x][weed_y] = "|"
board[weed_a][weed_b] = "|"
print_board(board)
for turn in range(4):
  print("Turn", turn + 1, "out of 4")
  guess_y = int(input("Guess Row: ")) - 1
  guess_x = int(input("Guess Col: ")) - 1

  if guess_x == weed_x and guess_y == weed_y or guess_x == weed_a and guess_y == weed_b:
    print("You got a weed!")
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
        break

    print_board(board)