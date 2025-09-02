class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs_visit(node, adj, visited):
            visited[node] = True

            for i in range(len(adj[0])):
                if adj[node][i] == 1 and not visited[i]:
                    dfs_visit(i, adj, visited)

        def dfs(adj):
            visited = [False] * len(adj)
            num_provinces = 0
            for i in range(len(adj)):
                if not visited[i]:
                    num_provinces += 1
                    dfs_visit(i, adj, visited)

            return num_provinces
        
        return dfs(isConnected)