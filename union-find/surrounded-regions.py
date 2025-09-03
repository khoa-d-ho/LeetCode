class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # start with 2d matrix iteration
        # if meet 0, perform traversal within
            # add every r c to visited set
            # create value is_edge
            # if r or c on the edge, is_edge = True
        # after island traversal
            # if is_edge == True:
                # skip
            # else: 
                # go through visited and turn 0 to x
        # continue until the end of the grid
        if not board:
            return

        moves = [(-1,0), (1, 0), (0, -1), (0, 1)]
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(r, c):
            # need nonlocal, since value is being reassigned. we are not creating new var named is_edge inside
            nonlocal is_edge # use for accessing values outside of nested funcitions
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] == "X" or (r,c) in visited:
                return 
            if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                is_edge = True

            # same object, just modified, no need for nonlocal
            visited.add((r, c)) 
            curr_region.append((r, c))
            
            for dr, dc in moves:
                nr = r + dr
                nc = c + dc
                dfs(nr, nc)


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in visited:
                    curr_region = []
                    is_edge = False
                    dfs(r,c)

                    if not is_edge:
                        for r, c in curr_region:
                            board[r][c] = "X"
