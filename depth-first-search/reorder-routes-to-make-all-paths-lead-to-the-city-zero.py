class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in connections:
            adj[a].append((b, 1))
            adj[b].append((a, 0))

        queue = deque()
        count = 0
        visit = [False] * n

        queue.append(0)
        visit[0] = True

        while queue:
            node = queue.popleft()
            print(node)
            for neighbor, sign in adj[node]:
                if not visit[neighbor]:
                    visit[neighbor] = True
                    count += sign
                    queue.append(neighbor)

        return count
        
        