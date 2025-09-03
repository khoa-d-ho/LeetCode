class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        moves = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        queue = collections.deque()
        starting = (entrance[0],entrance[1])

        queue.append((starting, 0))
        visited = {starting} # no duplicates

        while queue:
            coordinates, distance = queue.popleft()
            r, c = coordinates[0], coordinates[1]
            
            for di, dj in moves:
                cr, cc = r + di, c + dj
                if 0 <= cr < rows and 0 <= cc < cols and (cr, cc) not in visited:

                    if maze[cr][cc] == "+":
                        continue                         
                    if cr == 0 or cr == rows - 1 or cc == 0 or cc == cols - 1:
                        return distance + 1           

                    visited.add((cr, cc))
                    queue.append(((cr, cc), distance + 1))
        return -1