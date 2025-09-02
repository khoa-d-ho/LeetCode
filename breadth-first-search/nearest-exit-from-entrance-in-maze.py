class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        moves = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        queue = collections.deque()
        starting = (entrance[0],entrance[1])

        # for i in range(rows):
        #     for j in range(cols):
        #         if maze[i][j] == "*":
        #             starting = (i, j)
        #             break
        #     if starting:
        #         break

        queue.append((starting, 0))
        visited = {starting} # no duplicates

        while queue:
            coordinates, distance = queue.popleft()
            i, j = coordinates[0], coordinates[1]
            
            for di, dj in moves:
                ci, cj = i + di, j + dj
                if 0 <= ci < rows and 0 <= cj < cols and (ci, cj) not in visited:

                    if maze[ci][cj] == "+":
                        continue                         
                    if ci == 0 or ci == rows - 1 or cj == 0 or cj == cols - 1:
                        return distance + 1           

                    visited.add((ci, cj))
                    queue.append(((ci, cj), distance + 1))
        return -1