class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Moore Voting Algorithm
        current = 0 
        occurance = 0 
        for i in nums:
            if occurance == 0:
                current = i
            if i == current:
                occurance += 1
            else:
                occurance -= 1
        return current

        