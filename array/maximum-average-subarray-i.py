class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = 0
        left = 0
        max_sum = curr_sum = sum(nums[left:left + k])
        while left + k < len(nums):
            curr_sum += nums[left + k] - nums[left]
            max_sum = max(max_sum, curr_sum)
            left += 1


        return max_sum / k