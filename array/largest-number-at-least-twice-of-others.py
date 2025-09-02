class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_id = 0
        largest_num = nums[0]
        for i in range(len(nums)):
            if nums[i] > largest_num:
                largest_num = nums[i]
                max_id = i
                
        for n in nums:
            if 2 * n > largest_num and n != largest_num:
                return -1
            
            
        return max_id