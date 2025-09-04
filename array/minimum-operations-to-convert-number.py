from collections import deque:

class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        if start == goal:
            return 0
        elif not nums:
            return -1

        queue = deque()
        queue.append((start, 0))

        while queue:
            curr, ops = queue.popleft()
            for num in nums:
                queue.append((curr + num, ops + 1))