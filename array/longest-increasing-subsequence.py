class Solution:

    def lengthOfLIS(self, nums):
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            max_valid = 1
            for j in range(i):
                # compare nums
                if nums[i] > nums[j]:
                    # max
                    if dp[j] + 1 > max_valid:
                        max_valid = dp[j] + 1
            dp[i] = max_valid
        return max(dp)