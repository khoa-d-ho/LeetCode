class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # 1 0 1 0 1    goal = 2
      # 0 1 1 2 2 3 
      #-2-1-1 0 0 1
      #   0 1 2 3 4

      # 0:1
      # 1:2
      # 2:2
      # 3:1
        d = {0:1}
        prefix_sum = [0]
        ans = 0
        curr = 0
        for item in nums:
            curr += item
            if curr - goal in d:
                ans += d[curr - goal] 
            if curr not in d:
                d[curr] = 1
            else: 
                d[curr] += 1
        return ans