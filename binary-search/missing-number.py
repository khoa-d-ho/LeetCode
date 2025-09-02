class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        r = 0
        i = 0
        while i < len(nums):
            if nums[i] != r:
                return nums[i] - 1
            r += 1
            i += 1
        return nums[-1] + 1
