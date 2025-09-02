class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        
        memo = [[0] * (target + 1) for _ in range(n + 1)]
        memo[n][target] = 1
        for dice in reversed(range(n)):
            for sum in range(target):
                ways = 0

                for i in range(1, min(k, target - sum) + 1):
                    ways = (ways + memo[dice + 1][sum + i] ) % MOD

                memo[dice][sum] = ways

        return memo[0][0]
