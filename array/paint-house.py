class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [[0, 0, 0] for _ in range(len(costs) + 1)]
        for i in range(len(costs)):
            dp[i][0] = costs[i][0] + min(dp[i - 1][1], dp[i - 1][2])
            dp[i][1] = costs[i][1] + min(dp[i - 1][0], dp[i - 1][2])
            dp[i][2] = costs[i][2] + min(dp[i - 1][0], dp[i - 1][1])
            
        return min(dp[len(costs) - 1])