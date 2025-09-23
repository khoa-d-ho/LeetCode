class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 1 2 3
        # none, 1, 12, 123
        # 2, 23
         
        res = []
        n = len(nums)

        def backtrack(idx, curr):
            res.append(curr[:]) # dont reference current list
            print(res)
            for i in range(idx, n):
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop() # 12 13

        backtrack(0, [])
        return res
        