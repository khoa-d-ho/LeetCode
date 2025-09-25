from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 112 121, 211
        res = []
        n = len(nums)
        counts = Counter(nums)
        def backtrack(first, curr):
            if first == n:
                res.append(curr[:])

            tracer = set()
            for i in range(first, n):
                if curr[i] not in tracer:
                    tracer.add(nums[i])
                    curr[first], curr[i] = curr[i], curr[first]
                    backtrack(first + 1, curr)
                    curr[first], curr[i] = curr[i], curr[first]
        
        backtrack(0, nums[:])
        return res