import collections

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        moves = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        queue = collections.deque()
        starting = None

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "*":
                    starting = (i, j)
                    break
            if starting:
                break

        queue.append((starting, 0))
        visited = {starting} # no duplicates

        while queue:
            coordinates, distance = queue.popleft()
            i, j = coordinates[0], coordinates[1]
            
            for di, dj in moves:
                ci, cj = i + di, j + dj
                if 0 <= ci < rows and 0 <= cj < cols and (ci, cj) not in visited:
                    if grid[ci][cj] == "#":
                        return distance + 1
                    if grid[ci][cj] == "X":
                        continue                

                    visited.add((ci, cj))
                    queue.append(((ci, cj), distance + 1))
        return -1