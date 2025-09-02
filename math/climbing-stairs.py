import math
class Solution:
    def climbStairs(self, n: int) -> int:
        # the choose formula:
        # ex: 5 steps:
        # 2+1+1+1 is 4 choose 1
        # 2+2+1 is 3 choose 2

        ways = 0
        k = 0
        while n >= k:
            ways += math.factorial(n) / (
                (math.factorial(k)) * math.factorial(n - k)
            )
            n -= 1
            k += 1
        return int(ways)
