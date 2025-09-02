class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeroCount = 0
        longestWindow = 0
        start = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCount += 1
            
            while zeroCount > 1:
                if nums[start] == 0:
                    zeroCount -= 1
                start += 1

            longestWindow = max(longestWindow, i - start)

        return longestWindow