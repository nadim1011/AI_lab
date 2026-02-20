from collections import deque
class p8_board:
 def __init__(self, board, x, y, depth):
 self.board = board
 self.x = x
 self.y = y
 self.depth = depth
def is_valid(x, y):
 return 0 <= x < 3 and 0 <= y < 3
def is_goal(board):
 goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
 return board == goal
def bfs(start, x, y):
 queue = deque()
 queue.append(p8_board(start, x, y, 0))
 visited = set()
 visited.add(tuple(map(tuple, start)))
 row = [0, 0, -1, 1]
 col = [-1, 1, 0, 0]
 while queue:
 current = queue.popleft()
 if is_goal(current.board):
 print(f"Solution found at depth {current.depth}")
 return
 for i in range(4):
 new_x = current.x + row[i]
 new_y = current.y + col[i]
 if is_valid(new_x, new_y):
 new_board = [r[:] for r in current.board]
 new_board[current.x][current.y], new_board[new_x][new_y] = \
 new_board[new_x][new_y], new_board[current.x][current.y]
 board_tuple = tuple(map(tuple, new_board))
 if board_tuple not in visited:
 visited.add(board_tuple)
 queue.append(p8_board(new_board, new_x, new_y, current.depth + 1))
 print("No solution found")
# Example Run
start_board = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
bfs(start_board, 2, 1)
