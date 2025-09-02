class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        node_visited = 0
        queue = deque()
        visited = [0] * n
        queue.append(0)
        visited[0] = 1

        while queue:
            node = queue.popleft()
            node_visited += 1
            for neighbor in rooms[node]:
                if not visited[neighbor]:
                    visited[neighbor] = 1
                    queue.append(neighbor)

        return node_visited == n
            