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

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = UnionFind(n)

        for u, v in edges:
            graph.union(u, v)

        sets = {graph.find(u) for u in range(n)}
        return len(sets)