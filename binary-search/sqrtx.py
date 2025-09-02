class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x
        while start <= end:
            mid = (start + end)//2
            if mid ** 2 > x:
                end = mid - 1
            elif mid ** 2 < x:
                start = mid + 1
            else: return mid
        return end