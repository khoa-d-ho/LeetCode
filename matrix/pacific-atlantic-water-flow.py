from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # start from pacific edge 
        # do bfs for each of the coordinates 
            # if value equal or go up -> water can flow down the ocean
        # save to valid_p

        # do the same for atlantic
        # save to valid_a

        # values that in both valid_p and valid_a is res
        if not heights:
            return []
        moves = [(-1,0), (1, 0), (0, -1), (0, 1)]
        rows = len(heights)
        cols = len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()
        # coordinates_pacific = []
        # coordinates_atlantic = []

        def bfs(queue, visited):
            while queue:
                r, c = queue.popleft()
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            
            return visited

        pacific_queue = deque()
        for r in range(rows):
            pacific_queue.append((r, 0))
            pacific_reachable.add((r, 0))
        for c in range(1, cols): # already have (0,0)
            pacific_queue.append((0, c))
            pacific_reachable.add((0, c))
        
        bfs(pacific_queue, pacific_reachable)

        atlantic_queue = deque()
        for r in range(rows):
            atlantic_queue.append((r, cols - 1))
            atlantic_reachable.add((r, cols - 1))
        for c in range(cols - 1): # already have (rows - 1, cols - 1)
            atlantic_queue.append((rows - 1, c))
            atlantic_reachable.add((rows - 1, c))
        
        bfs(atlantic_queue, atlantic_reachable)

        return list(pacific_reachable & atlantic_reachable)


                