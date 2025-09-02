class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        f1 = float("inf")
        s2 = float("inf")
        for n in nums:
            if n <= f1:
                f1 = n
            elif n <= s2:
                s2 = n
            else: 
                return True
            
        return False