class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 123, 
        # 132, 
        # 213, 
        # 231, 
        # 312, 
        # 321

        res = []
        n = len(nums)

        def backtrack(first, curr):
            if first == n -1:
                res.append(curr[:]) 
                
            for i in range(first, n):
                curr[first], curr[i] = curr[i], curr[first]
                backtrack(first + 1, curr)
                curr[first], curr[i] = curr[i], curr[first]
        backtrack(0, nums[:])
        return res