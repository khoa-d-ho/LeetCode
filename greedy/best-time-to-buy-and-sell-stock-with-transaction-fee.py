class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0, 0] for _ in range(len(prices) + 1)]
        
        for i in reversed(range(len(prices))):
                dp[i][0] = max(dp[i + 1][0], dp[i + 1][1] - prices[i])
                dp[i][1] = max(dp[i + 1][1], dp[i + 1][0] + prices[i] - fee)
                    
                    
        return dp[0][0]
