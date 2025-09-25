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


# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         # 1 2 3
#         # none, 1, 12, 123
#         # 2, 23
         
#         res = []
#         n = len(nums)

#         def backtrack(idx, curr):
#             res.append(curr[:]) # dont reference current list
#             for i in range(idx, n):
#                 curr.append(nums[i])
#                 backtrack(i+1, curr)
#                 curr.pop() # 12 13

#         backtrack(0, [])
#         return res