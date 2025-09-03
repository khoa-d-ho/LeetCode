class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # loop through matrix
        # if land, run dfs to get all lands
        if not grid: 
            return 0
        rows = len(grid)
        cols = len(grid[0])
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        r = 0
        c = 0
        res = 0
        def dfs(r, c, grid):
            if r >= rows or c >= cols or grid[r][c] == '0' or r < 0 or c < 0:
                return
            grid[r][c] = '0'
            for dr, dc in moves:
                dfs(r + dr, c + dc, grid)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    res += 1 
                    dfs(r, c, grid)

        return res
