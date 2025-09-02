class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[0:k]
        heapq.heapify(heap)

        for item in nums[k:]:
            if item > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, item)
        return heap[0]