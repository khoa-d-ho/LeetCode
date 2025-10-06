class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        # dp =   [1,1,1,2,2,3,4,5,5]
        # nums = [4,2,1,4,3,4,5,8,15], k = 3
        #               i
        #             j 
        # dp[i] = max(dp[j] + 1, dp[i])

        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            curr_max = 1
            for j in range(i):
                if 0 < nums[i] - nums[j] <= k:
                    if curr_max < dp[j] + 1:
                        curr_max = dp[j] + 1
            dp[i] = curr_max
        print(dp)
        return max(dp)
                
                