class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        

        self.rows = len(board)
        self.cols = len(board[0])

        from itertools import product

        borders = list(product(range(0, self.rows), [0, self.cols - 1])) + list(product([0, self.rows - 1], range(0, self.cols)))

        for r, c in borders:
            self.DFS(board, r, c)

        for r in range(self.rows):
            for c in range(self.cols):
                if board[r][c] == "O":
                    board[r][c] = "X"  # captured
                elif board[r][c] == "E":
                    board[r][c] = "O"  # escaped 

    def DFS(self, board, row, col):
        if board[row][col] != "O":
            return
        
        board[row][col] = "E"
        if row < self.rows - 1:
            self.DFS(board, row + 1, col)
        if col < self.cols - 1:
            self.DFS(board, row, col + 1)
        if row > 0:
            self.DFS(board, row - 1, col)
        if col > 0:
            self.DFS(board, row, col - 1)