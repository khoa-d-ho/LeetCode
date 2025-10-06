class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # nums = [1,3,5,4,7]
        # dp =   [1,2,3,3,4]

        # 2 2 2 2 2
        # 1 1 1 1 1

        # [10,9,2,5,3,7,101,18]
        #   1 1 1 2 2 3 4    4

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
        
        largest = float("-inf")
        second_largest = float("-inf")
        largest_freq = 0
        second_largest_freq = 0
        for num in dp:
            if num > largest:
                second_largest = largest
                second_largest_freq = largest_freq
                largest = num
                largest_freq = 1
            elif num == largest:
                largest_freq += 1
            elif num > second_largest:
                second_largest = num
                second_largest_freq = 1
            elif num == second_largest:
                second_largest_freq += 1
        if second_largest_freq == 0:
            return largest_freq
        return second_largest_freq


        
        