class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        adj_list = [set() for _ in range(n)]

        for a, b in edges:
            adj_list[a].add(b)
            adj_list[b].add(a)
        
        leaves = []
        for i in range(n):
            if len(adj_list[i]) == 1:
                leaves.append(i)

        remaining_nodes = n
        while remaining_nodes > 2:
            new_leaves = []
            remaining_nodes -= len(leaves)

            while leaves:
                leaf = leaves.pop()

                neighbor = adj_list[leaf].pop()
                adj_list[neighbor].remove(leaf)
                if len(adj_list[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves
        
        return leaves
                
        

        
                

        

        