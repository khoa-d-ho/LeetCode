class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        queue = collections.deque()
        starting = (0,0)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j] == "*":
        #             starting = (i, j)
        #             break
        #     if starting:
        #         break

        queue.append((starting, 1))
        visited = {starting} # no duplicates

        while queue:
            coordinates, distance = queue.popleft()
            i, j = coordinates[0], coordinates[1]
            if i == n - 1 and j == n - 1:
                return distance
            
            for di, dj in moves:
                ci, cj = i + di, j + dj
                if 0 <= ci < n and 0 <= cj < n and grid[ci][cj] == 0 and (ci, cj) not in visited:

                    visited.add((ci, cj))
                    queue.append(((ci, cj), distance + 1))
                    
        return -1