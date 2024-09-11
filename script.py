from connect_four import *

def two_ai_game():
    my_board = make_board()
    while not game_is_over(my_board):
      #The "X" player finds their best move.
      result = minimax(my_board, True, 4, -float("Inf"), float("Inf"), my_evaluation_board)
      print( "X Turn\nX selected ", result[1])
      print(result[1])
      select_space(my_board, result[1], "X")
      print_board(my_board)

      if not game_is_over(my_board):
        #The "O" player finds their best move
        result = minimax(my_board, False, 1, -float("Inf"), float("Inf"), codecademy_evaluate_board)
        print( "O Turn\nO selected ", result[1])
        print(result[1])
        select_space(my_board, result[1], "O")
        print_board(my_board)
    if has_won(my_board, "X"):
        print("X won!")
    elif has_won(my_board, "O"):
        print("O won!")
    else:
        print("It's a tie!")

#An function is the algorithm to determine who wins. There are two ways to winning 
#if X won by getting 4 streaks then the evaluation function returns Inf
#if O won by getting 4 streaks, then the evaluation function returns -Inf
def my_evaluation_board(board):
  if has_won(board,'X'):
    return float('Inf')
  elif has_won(board,'O'):
    return -float('Inf')
  x_two_streak,o_two_streak = 0,0

# Looping to check if any two box from left to right have the same pieces
# to determine who has a higher chance of winning 
# If X has the most number of two streaks, then X also wins
#If O has the most number of two streak, then O alos wins 
  for col in range(len(board) -1):
    for row in range(len(board[0])):
    # Check the value of board[col][row]
      if board[col][row] and board[col + 1][row]=='X':
        x_two_streak +=1
      elif board[col][row] and board[col + 1][row]=='O':
        o_two_streak +=1
  return  x_two_streak-o_two_streak

two_ai_game()
# new_board = make_board()
# select_space(new_board, 5, "O")
# select_space(new_board, 6, "O")
# select_space(new_board, 6, "O")
# select_space(new_board, 6, "O")
# select_space(new_board, 6, "O")
# print_board(new_board)
# print(my_evaluation_board(new_board))
