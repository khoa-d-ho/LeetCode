class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        stack = [0]

        while stack:
            room_idx = stack.pop()
            for key in rooms[room_idx]:
                if key not in visited:
                    visited.add(key)
                    stack.append(key)
        
        return len(visited) == len(rooms)

