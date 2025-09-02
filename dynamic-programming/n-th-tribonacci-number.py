class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [0, 1, 1]
        i = 3
        while i < n + 1:
            memo.append(memo[i - 1] + memo[i - 2] + memo[i - 3]) 
            i += 1

        return memo[n]
        