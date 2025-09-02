class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False

        seen = {0}
        q = deque([0])
        # q.append(0)

        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)

        while q:
            node = q.popleft()
            for neighbor in adj_list[node]:
                if neighbor in seen:
                    continue
                seen.add(neighbor)
                q.append(neighbor)

                
        return len(seen) == n