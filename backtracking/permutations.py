class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0 or len(nums) == 1:
            return [nums]
        
        perms = self.permute(nums[1:])
        result = []

        for perm in perms:
            for slot in range(len(nums)):
                perm_copy = perm.copy()
                perm_copy.insert(slot, nums[0])
                result.append(perm_copy)
        return result


        
        