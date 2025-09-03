class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        queue = collections.deque()
        starting = (0,0)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        queue.append((starting, 1))
        visited = {starting} # no duplicates

        while queue:
            coordinates, distance = queue.popleft()
            r, c = coordinates[0], coordinates[1]
            if r == n - 1 and c == n - 1:
                return distance
            
            for di, dj in moves:
                cr, cc = r + di, c + dj
                if 0 <= cr < n and 0 <= cc < n and grid[cr][cc] == 0 and (cr, cc) not in visited:

                    visited.add((cr, cc))
                    queue.append(((cr, cc), distance + 1))
                    
        return -1