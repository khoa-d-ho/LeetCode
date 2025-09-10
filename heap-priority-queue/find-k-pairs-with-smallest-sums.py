import heapq
from collections import deque

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # nums1 = [1,7,11]
        # nums2 = [2,4,6]
        # heap = 
        # (sum, [1,1])
        
        nums1 = deque(nums1)
        nums2 = deque(nums2)

        heap = [(nums1[0] + nums2[0], 0, 0)]
        heapq.heapify(heap)

        i = 0
        res = []
        visited = {(0,0)}

        while len(res) < k and heap:
            total, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            
            if i < len(nums1) - 1 and (i + 1, j) not in visited:
                total = nums1[i + 1] + nums2[j]
                heapq.heappush(heap, (total, i + 1, j))
                visited.add((i + 1, j))

            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                total = nums1[i] + nums2[j + 1]
                heapq.heappush(heap, (total, i, j + 1))
                visited.add((i, j + 1))
        
        return res
        