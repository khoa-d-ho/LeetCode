class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(prices) + 2)]
        print(dp)
        for i in range(len(prices) - 1, -1, -1):
            for holding in range(2):
                donothing = dp[i + 1][holding]
                dosomething = 0
                if holding:
                    dosomething = prices[i] + dp[i + 2][0]
                
                else:
                    dosomething = -prices[i] + dp[i + 1][1]
                    
                dp[i][holding] = max(dosomething, donothing)
                    
        return dp[0][0]