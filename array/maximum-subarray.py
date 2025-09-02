class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = float("-inf")
        current = 0
        for num in nums:
            current = max(current + num, num)
            best = max(best, current)


        return best