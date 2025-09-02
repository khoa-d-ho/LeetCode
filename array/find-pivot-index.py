class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            if left_sum == total - nums[i]:
                return i
            else:
                left_sum += nums[i]
                total -= nums[i]
                
        return -1