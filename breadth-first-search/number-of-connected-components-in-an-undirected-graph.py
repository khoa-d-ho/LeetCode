class UnionFind:
    def __init__(self, n): # n = 3
        self.parent = [i for i in range(n)] # [1,1,2]

    def find(self, x): # x = 2
        if x != self.parent[x]:
            return self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b): #
        ra = self.find(a)
        rb = self.find(b)
        self.parent[rb] = self.parent[ra]

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = UnionFind(n)

        for u, v in edges:
            graph.union(u, v)

        sets = {graph.find(u) for u in range(n)}
        return len(sets)