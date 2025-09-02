class Solution:
    def numWays(self, n: int, k: int) -> int:
        one_back = k*k
        two_back = k
        if n == 0:
            return 0
        if n == 1:
            return two_back
        
        for i in range(2, n):
            temp = one_back
            one_back = (k - 1) * (one_back + two_back)
            two_back = temp
            
        return one_back
        