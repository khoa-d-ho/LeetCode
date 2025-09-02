class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [1]
        for item in nums:
            prefix_prod.append(prefix_prod[-1]  * item)
        
        suffix_prod = deque()
        suffix_prod.append(1)
        for i in range(len(nums) - 1, -1, -1):
            suffix_prod.appendleft(suffix_prod[0]  * nums[i])

        res = []
        for i in range(len(nums)): 
            if i == 0:
                res.append(suffix_prod[i+1])
            elif i == len(nums) - 1:
                res.append(prefix_prod[i])
            else:
                res.append(prefix_prod[i] * suffix_prod[i+1])
        return res
