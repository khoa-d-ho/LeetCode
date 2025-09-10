import heapq
from collections import deque

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # nums1 = [1,2], nums2 = [2,3], k = 2
        # heap = 1,1
        # (sum, [1,1])

        heap = [(nums1[0] + nums2[0], [nums1[0], nums2[0]])]
        heapq.heapify(heap)

        nums1.deque()
        nums2.deque()

        while nums1:
            num1, num2 = heapq.heappop(heap)
            next1 = nums1.popleft()
            next2 = nums2.popleft()
            heapq.heappush((num1 + next1, [num1, next1]))
            heapq.heappush((num1 + next1, [num1, next1]))heapq.heappush((num1 + next1, [num1, next1]))