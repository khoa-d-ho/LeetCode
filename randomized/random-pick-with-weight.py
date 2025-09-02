import random

class Solution:

    def __init__(self, w: List[int]):
        # prefix sum
        self.prefix_sum = [w[0]]
        for item in w[1:]:
            self.prefix_sum.append(self.prefix_sum[-1] + item)
        # 0 20 60 100
    def pickIndex(self) -> int:
        target = random.randint(1, self.prefix_sum[-1]) # no zero
        # binary search
        left = 0
        right = len(self.prefix_sum) - 1
        while left <= right:
            mid = (left + right) // 2
            if target > self.prefix_sum[mid]:
                left = mid + 1
            elif target < self.prefix_sum[mid]:
                right = mid - 1
            else: 
                return mid
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()