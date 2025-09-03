class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # not graph traversal !?
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    for dr, dc in moves:
                        nr = r + dr
                        nc = c + dc
                        if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0:
                            res += 1
                            
        return res
                    