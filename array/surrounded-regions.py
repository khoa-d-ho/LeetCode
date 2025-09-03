from typing import List
import collections

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # start with 2d matrix iteration
        # if meet O, perform traversal within
            # add every r c to visited set
            # create value is_edge
            # if r or c on the edge, is_edge = True
        # after island traversal
            # if is_edge == True:
                # skip
            # else: 
                # go through visited and turn O to x
        # continue until the end of the grid
        if not board:
            return

        moves = [(-1,0), (1, 0), (0, -1), (0, 1)]
        rows = len(board)
        cols = len(board[0])
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in visited:
                    curr_region = []
                    is_edge = False
                    
                    stack = [(r, c)]
                    visited.add((r, c))

                    while stack:
                        row, col = stack.pop()
                        curr_region.append((row, col))
                        
                        if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                            is_edge = True
                        
                        for dr, dc in moves:
                            nr, nc = row + dr, col + dc
                            if 0 <= nr < rows and 0 <= nc < cols and \
                               board[nr][nc] == 'O' and (nr, nc) not in visited:
                                
                                visited.add((nr, nc))
                                stack.append((nr, nc))
                                
                    if not is_edge:
                        for row, col in curr_region:
                            board[row][col] = "X"