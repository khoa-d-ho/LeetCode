class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if x != self.parent[x]:
            return self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        self.parent[rb] = self.parent[ra]
        return True

# Input: logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4
# Output: 3

# 0 1 2 3 
# [2, 2, 2, 2]

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        last_true = 0
        graph = UnionFind(n)

        for time, a, b in logs:
            if graph.union(a, b):
                last_true = time
        
        sets = {graph.find(u) for u in range(n)}
        if len(sets) > 1:
            return -1
        else:
            return last_true