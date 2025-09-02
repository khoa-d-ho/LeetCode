class Solution:
    def minOperations(self, nums: List[int]) -> int:
        total_ops = 0 
        nums_copy = nums.copy()
        if len(nums) <= 1:
            return total_ops
        for i in range(1, len(nums)):
            if nums_copy[i - 1] >= nums_copy[i]:
                total_ops += nums_copy[i - 1] - nums_copy[i] + 1
                nums_copy[i] = nums_copy[i - 1] + 1
        return total_ops