N = 4

def is_valid(board, row, col):
  for i in range(len(board)):
    if board[i][col] == 'Q':
      return False
  
  i = row
  j = col
  while i >= 0 and j >= 0:
    if board[i][j] == 'Q':
      return False
    i -= 1
    j -= 1

  i = row
  j = col 
  while j >= 0 and i < len(board):
    if board[i][j] == 'Q':
      return False
    i += 1
    j -= 1

  return True

def solve_nq(board, col):
  res = []
  if col >= len(board):
    copy = ["".join(row) for row in board]
    res.append(copy)
    return res

  for i in range(len(board)):
    if is_valid(board, i, col):
      board[i][col] = 'Q'
      solutions = solve_nq(board, col + 1)
      res.extend(solutions)
      board[i][col] = '.'

  return res

board = [['.' for i in range(N)] for j in range(N)]
solutions = solve_nq(board, 0)
print(solutions)