class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        sa = self.size[ra]
        sb = self.size[rb]
        if sa < sb:
            ra, rb = rb, ra
        self.size[rb] += self.size[ra]
        self.size[ra] = self.size[rb]
        self.parent[rb] = self.parent[ra]
        
        return True

# Input: logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4
# Output: 3

# 0 1 2 3 
# [2, 2, 2, 2]

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        graph = UnionFind(n)
        set_count = n
        
        for time, a, b in logs:
            if graph.union(a, b):
                set_count -= 1
                if set_count == 1:
                    return time
        
        return -1