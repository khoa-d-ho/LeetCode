class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        l = r = 0
        ans = float("inf")
        curr_sum = nums[0]
        while r < len(nums):
            if curr_sum >= target:
                ans = min(ans, r - l + 1)
                l += 1
                curr_sum -= nums[l-1]
            else:
                r += 1
                if r >= len(nums):
                    break
                curr_sum += nums[r]

        return 0 if ans == float("inf") else ans