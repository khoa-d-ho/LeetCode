from collections import deque

class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        if not nums:
            return -1

        queue = deque()
        queue.append((start, 0))
        visited = {start}

        while queue:
            curr, ops = queue.popleft()
            if curr == goal:
                return ops
            for num in nums:
                operations = [curr + num, curr - num, curr ^ num]
                for result in operations:
                    if result == goal:
                        return ops + 1
                    if not (0 <= result <= 1000) or result in visited:
                        break
                    visited.add(result)
                    queue.append((result, ops + 1))
        return -1