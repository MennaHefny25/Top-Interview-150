"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised 

by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: 

live (represented by a 1) or dead (represented by a 0). 

Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) 

using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.

Any live cell with two or three live neighbors lives on to the next generation.

Any live cell with more than three live neighbors dies, as if by over-population.

Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state is created by applying the above rules simultaneously to every cell in the current state, 

where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

 

Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
"""

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # Dimensions of the board
        m, n = len(board), len(board[0])
        
        # Define the 8 possible directions (neighbors)
        directions = [
            (-1, -1), (-1, 0), (-1, 1),  # top-left, top, top-right
            (0, -1),           (0, 1),   # left,       , right
            (1, -1), (1, 0), (1, 1)      # bottom-left, bottom, bottom-right
        ]
        
        # Helper function to count live neighbors
        def count_live_neighbors(x, y):
            live_neighbors = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Check bounds and if the cell is currently alive
                if 0 <= nx < m and 0 <= ny < n and abs(board[nx][ny]) == 1:
                    live_neighbors += 1
            return live_neighbors
        
        # First pass to determine the next state
        for i in range(m):
            for j in range(n):
                live_neighbors = count_live_neighbors(i, j)
                
                # Apply the rules of the Game of Life
                if board[i][j] == 1:  # Live cell
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = -1  # Mark as dead in next state
                else:  # Dead cell
                    if live_neighbors == 3:
                        board[i][j] = 2  # Mark as alive in next state
        
        # Second pass to finalize the board
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0  # Update to dead
                elif board[i][j] == 2:
                    board[i][j] = 1  # Update to live

        return board 

sol = Solution()
# Example 1: Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]

print(sol.gameOfLife(board=board))

# Example 2: Output: [[1,1],[1,1]]
board = [[1,1],[1,0]]

print(sol.gameOfLife(board=board))